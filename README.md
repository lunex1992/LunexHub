# Django Todo List

Python Django 기반 Todo List 일정관리 웹 애플리케이션입니다.

## Tech Stack

- Python
- Django
- MySQL
- Git
- GitHub

## Project Goals

- Todo 생성, 수정, 삭제
- 일정 관리
- 사용자 로그인 및 인증
- MySQL 데이터베이스 연동
- 테스트 및 CI/CD 구축
- Docker 컨테이너화
- 클라우드 배포
- Kubernetes 적용

- # LunexHub - Day 002

## 학습 목표
Django 애플리케이션 생성 및 URL과 View 연결

## 구현 내용
- todo 앱 생성
- INSTALLED_APPS 등록
- 첫 번째 View 구현
- URL 라우팅 구성
- HttpResponse 출력

## 배운 개념
- Django Project와 App의 차이
- HTTP Request와 Response
- URL Routing
- Django View
- include() 함수

## Git Commit
feat: create todo app and first view

## 다음 목표
Django Template을 사용하여 HTML 페이지 만들기

# LunexHub - Day 003

## 학습 목표

Django Template과 Context를 활용한 동적 HTML 페이지 구현 및 자동화 테스트 작성

## 구현 내용

- `todo/templates/todo/index.html` 생성
- HTML 기본 구조 작성
- `HttpResponse()`에서 `render()`로 View 변경
- Context 딕셔너리를 활용한 데이터 전달
- `{{ username }}`, `{{ todo_count }}`를 이용한 동적 데이터 출력
- Django `TestCase`를 활용한 자동화 테스트 작성
- HTTP 응답 상태 코드 및 페이지 내용 검증

## 배운 개념

- Django Template
- `render()` 함수
- Python Dictionary (`dict`)
- Context와 Template Variable
- Django Template의 `{{ }}` 문법
- View와 Template의 역할 분리
- Django `TestCase`
- `reverse()` 함수
- `assertEqual()` 및 `assertContains()`

## 전력 ICT TA 학습

- HTTP Request와 Response 구조
- IP 주소와 포트의 개념
- 루프백 IP (`127.0.0.1`)
- HTTP 상태 코드 (`200`, `301`, `404`, `500`)
- URL 리다이렉트와 `APPEND_SLASH`
- `curl`을 활용한 HTTP 응답 확인
- 개발 서버와 운영 서버의 차이

## 테스트 및 검증

- `python manage.py check`
- `python manage.py test todo`
- `python manage.py runserver`
- `curl -i http://127.0.0.1:8000/todo/`
- `curl -IL http://127.0.0.1:8000/todo`

## Git Commit

`feat: add todo template and view tests`

## 다음 목표

HTML Form을 활용한 Todo 입력 기능 구현 및 HTTP GET/POST, CSRF 보안 개념 학습
