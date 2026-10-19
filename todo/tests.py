from django.test import TestCase
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
        self.assertContains(response, '현재 등록된 할 일: 5개')