from django.test import TestCase, Client
#Client: 실제 브라우저 없이 HTTP 요청을 흉내 내는 테스트 도구
from django.urls import reverse

# Create your tests here.
class TodoViewTests(TestCase):

#self는 현재 테스트 클래스의 인스턴스
#self.client는 Django 테스트용 HTTP 클라이언트
#reverse()는 URL에 부여한 이름을 실제 경로로 변환합니다.
    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Welcome, Lunex!')
        self.assertContains(response, '현재 등록된 할 일: 3개')

    def test_get_todo_title(self):
        response = self.client.get(
            reverse('index'),
            {'title': 'Django GET 공부'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '입력한 할 일: Django GET 공부')

    def test_post_todo_title(self):
        response = self.client.post(
            reverse('index'),
            {'title': 'Django POST 공부'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '입력한 할 일: Django POST 공부')

    def test_post_without_csrf_token(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse('index'),
            {'title': 'CSRF Test'}
        )

        self.assertEqual(response.status_code, 403)
