from django.test import Client, TestCase
from django.urls import reverse

from .models import Todo


class TodoViewTests(TestCase):

    #001
    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    #002
    def test_index_page_content(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'Welcome, Lunex!')
        self.assertContains(response, '현재 등록된 할 일: 0개')

    #003
    def test_get_does_not_create_todo(self):
        response = self.client.get(
            reverse('index'),
            {'title': 'GET으로 전달한 Todo'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 0)

    #004
    def test_post_creates_todo_and_redirects(self):
        response = self.client.post(
            reverse('index'),
            {'title': 'Django ORM 공부하기'}
        )

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(
            Todo.objects.first().title,
            'Django ORM 공부하기'
        )

    #005
    def test_post_without_csrf_token(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse('index'),
            {'title': 'CSRF Test'}
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Todo.objects.count(), 0)

    #006
    def test_post_blank_title_does_not_create_todo(self):
        response = self.client.post(
            reverse('index'),
            {'title': '   '}
        )

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Todo.objects.count(), 0)

    #007
    def test_index_displays_saved_todos(self):
        Todo.objects.create(title='운동하기')
        Todo.objects.create(title='기타 연습하기')

        response = self.client.get(reverse('index'))

        self.assertContains(response, '운동하기')
        self.assertContains(response, '기타 연습하기')
        self.assertContains(response, '현재 등록된 할 일: 2개')

    #008
    def test_newest_todo_appears_first(self):
        Todo.objects.create(title='첫 번째 Todo')
        Todo.objects.create(title='두 번째 Todo')

        response = self.client.get(reverse('index'))

        self.assertContains(
            response,
            '두 번째 Todo',
            html=False
        )

        todos = list(response.context['todos'])

        self.assertEqual(todos[0].title, '두 번째 Todo')
        self.assertEqual(todos[1].title, '첫 번째 Todo')

    #009
    def test_post_toggles_todo_to_completed(self):
        todo = Todo.objects.create(title='운동하기')

        response = self.client.post(
            reverse('toggle_todo', args=[todo.id])
        )

        self.assertRedirects(response, reverse('index'))

        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

    #010
    def test_post_toggles_completed_todo_to_incomplete(self):
        todo = Todo.objects.create(
            title='기타 연습하기',
            is_completed=True
        )

        response = self.client.post(
            reverse('toggle_todo', args=[todo.id])
        )

        self.assertRedirects(response, reverse('index'))

        todo.refresh_from_db()
        self.assertFalse(todo.is_completed)

    #011
    def test_get_cannot_toggle_todo(self):
        todo = Todo.objects.create(title='Django 공부하기')

        response = self.client.get(
            reverse('toggle_todo', args=[todo.id])
        )

        self.assertEqual(response.status_code, 405)

        todo.refresh_from_db()
        self.assertFalse(todo.is_completed)

    #012
    def test_toggle_nonexistent_todo_returns_404(self):
        response = self.client.post(
            reverse('toggle_todo', args=[999999])
        )

        self.assertEqual(response.status_code, 404)

    #013
    def test_post_deletes_todo(self):
        todo = Todo.objects.create(title='삭제할 Todo')
        todo_id = todo.id

        response = self.client.post(
            reverse('delete_todo', args=[todo_id])
        )

        self.assertRedirects(response, reverse('index'))
        self.assertFalse(
            Todo.objects.filter(pk=todo_id).exists()
        )

    #014
    def test_get_cannot_delete_todo(self):
        todo = Todo.objects.create(title='보존할 Todo')

        response = self.client.get(
            reverse('delete_todo', args=[todo.id])
        )

        self.assertEqual(response.status_code, 405)
        self.assertTrue(
            Todo.objects.filter(pk=todo.id).exists()
        )

    #015
    def test_delete_nonexistent_todo_returns_404(self):
        response = self.client.post(
            reverse('delete_todo', args=[999999])
        )

        self.assertEqual(response.status_code, 404)

    #016
    def test_delete_without_csrf_token_returns_403(self):
        todo = Todo.objects.create(title='CSRF 보호 테스트')

        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse('delete_todo', args=[todo.id])
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Todo.objects.filter(pk=todo.id).exists()
        )
