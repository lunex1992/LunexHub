from django.test import Client, TestCase
from django.urls import reverse

from .models import Todo


class TodoViewTests(TestCase):

    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_index_page_content(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'Welcome, Lunex!')
        self.assertContains(response, '현재 등록된 할 일: 0개')

    def test_get_does_not_create_todo(self):
        response = self.client.get(
            reverse('index'),
            {'title': 'GET으로 전달한 Todo'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 0)

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

    def test_post_without_csrf_token(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse('index'),
            {'title': 'CSRF Test'}
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Todo.objects.count(), 0)

    def test_post_blank_title_does_not_create_todo(self):
        response = self.client.post(
            reverse('index'),
            {'title': '   '}
        )

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Todo.objects.count(), 0)

    def test_index_displays_saved_todos(self):
        Todo.objects.create(title='운동하기')
        Todo.objects.create(title='기타 연습하기')

        response = self.client.get(reverse('index'))

        self.assertContains(response, '운동하기')
        self.assertContains(response, '기타 연습하기')
        self.assertContains(response, '현재 등록된 할 일: 2개')

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