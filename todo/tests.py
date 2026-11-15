from datetime import date

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

    # DAY 007 / STEP 006-1
    # Todo 제목 수정 자동화 테스트
    # 테스트가 끝나면 테스트용 데이터는 정리되므로 실제 Todo 데이터에는 영향을 주지 않습니다.
    #017
    def test_post_edits_todo_title(self):
        todo = Todo.objects.create(title='Original Title')

        # reverse()는 URL 이름을 실제 경로로 변환합니다.
        response = self.client.post(
            reverse('edit_todo', args=[todo.id]),
            {'title': 'Updated Title'}
        )

        # Python 객체에 DB 최신 값 반영
        todo.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(todo.title, 'Updated Title')

    #018
    def test_get_cannot_edit_todo(self):
        todo = Todo.objects.create(title='Original Title')

        response = self.client.get(
            reverse('edit_todo', args=[todo.id])
        )

        todo.refresh_from_db()

        self.assertEqual(response.status_code, 405)
        self.assertEqual(todo.title, 'Original Title')

    #019
    def test_edit_nonexistent_todo_returns_404(self):
        response = self.client.post(
            reverse('edit_todo', args=[999999]),
            {'title': 'Updated Title'}
        )

        self.assertEqual(response.status_code, 404)

    #020
    def test_post_blank_title_does_not_edit_todo(self):
        todo = Todo.objects.create(title='Original Title')

        response = self.client.post(
            reverse('edit_todo', args=[todo.id]),
            {'title': '   '}
        )

        todo.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(todo.title, 'Original Title')

    #021
    def test_edit_preserves_other_todo_fields(self):
        from datetime import date

        todo = Todo.objects.create(
            title='Original Title',
            is_completed=True,
            scheduled_date=date(2026, 11, 15)
        )

        response = self.client.post(
            reverse('edit_todo', args=[todo.id]),
            {'title': 'Updated Title'}
        )

        todo.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(todo.title, 'Updated Title')
        self.assertTrue(todo.is_completed)
        self.assertEqual(
            todo.scheduled_date,
            date(2026, 11, 15)
        )

    # DAY 007 / STEP 006-2
    # Todo 예정 날짜 생성 및 저장 자동화 테스트
    #022
    def test_post_creates_todo_with_scheduled_date(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Django Study',
                'scheduled_date': '2026-11-15'
            }
        )

        todo = Todo.objects.get(title='Django Study')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            todo.scheduled_date,
            date(2026, 11, 15)
        )

    #023
    def test_post_creates_todo_without_scheduled_date(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Exercise',
                'scheduled_date': ''
            }
        )

        todo = Todo.objects.get(title='Exercise')

        self.assertEqual(response.status_code, 302)
        self.assertIsNone(todo.scheduled_date)

    #024
    def test_post_without_date_field_creates_todo(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Old Style Todo'
            }
        )

        todo = Todo.objects.get(title='Old Style Todo')

        self.assertEqual(response.status_code, 302)
        self.assertIsNone(todo.scheduled_date)

    #025
    def test_multiple_todos_preserve_individual_dates(self):
        self.client.post(
            reverse('index'),
            {
                'title': 'First Todo',
                'scheduled_date': '2026-11-15'
            }
        )

        self.client.post(
            reverse('index'),
            {
                'title': 'Second Todo',
                'scheduled_date': '2026-11-20'
            }
        )

        first_todo = Todo.objects.get(title='First Todo')
        second_todo = Todo.objects.get(title='Second Todo')

        self.assertEqual(
            first_todo.scheduled_date,
            date(2026, 11, 15)
        )

        self.assertEqual(
            second_todo.scheduled_date,
            date(2026, 11, 20)
        )

        self.assertEqual(Todo.objects.count(), 2)        

    # DAY 007 / STEP 006-3
    # 날짜 유효성 및 HTML 출력 자동화 테스트
    #026
    def test_post_rejects_nonexistent_date(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Invalid Calendar Date',
                'scheduled_date': '2026-02-30'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Todo.objects.filter(
                title='Invalid Calendar Date'
            ).exists()
        )
    #assertFalse()는 잘못된 날짜를 가진 Todo가 생성되지 않았는지 확인합니다.

    #027
    def test_post_rejects_invalid_date_format(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Invalid Date Format',
                'scheduled_date': 'not-a-date'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Todo.objects.filter(
                title='Invalid Date Format'
            ).exists()
        )

    #028
    def test_post_accepts_valid_leap_day(self):
        response = self.client.post(
            reverse('index'),
            {
                'title': 'Leap Day Todo',
                'scheduled_date': '2028-02-29'
            }
        )

        todo = Todo.objects.get(
            title='Leap Day Todo'
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            todo.scheduled_date,
            date(2028, 2, 29)
        )

    #029
    def test_index_displays_scheduled_date(self):
        Todo.objects.create(
            title='Scheduled Todo',
            scheduled_date=date(2026, 11, 15)
        )

        response = self.client.get(
            reverse('index')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '예정일: 2026-11-15'
        )

    #030
    def test_index_displays_unscheduled_label(self):
        Todo.objects.create(
            title='Unscheduled Todo',
            scheduled_date=None
        )

        response = self.client.get(
            reverse('index')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '예정일: 미지정'
        )        