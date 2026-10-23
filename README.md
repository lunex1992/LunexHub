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

# LunexHub - Day 004

## 학습 목표
- HTML Form을 이용한 사용자 입력 처리
- HTTP GET과 POST 요청의 차이 이해
- Django `request.GET`, `request.POST` 활용
- CSRF 보안의 원리 이해
- Django 자동화 테스트 및 GitHub PR 실습

## 구현 내용
- Todo 입력을 위한 HTML Form 구현
- GET 요청의 Query String 데이터 처리
- POST 요청의 Form 데이터 처리
- `{% csrf_token %}`을 이용한 CSRF 보호
- `.strip()`을 이용한 입력값 앞뒤 공백 제거
- 입력한 Todo를 HTML Template에 출력

※ 현재 Todo 데이터는 화면에 출력되며, 데이터베이스에는 저장하지 않음.

## 배운 개념
- **HTTP GET**: 서버의 리소스를 조회할 때 사용하는 HTTP 메서드
- **HTTP POST**: 서버에 데이터를 제출하여 처리하도록 요청하는 HTTP 메서드
- **request.GET**: URL Query String 매개변수에 접근하는 Django QueryDict
- **request.POST**: POST Form 데이터에 접근하는 Django QueryDict
- **request.method**: 현재 HTTP 요청의 메서드 확인
- **CSRF**: 사용자가 의도하지 않은 요청을 유도하는 사이트 간 요청 위조 공격
- **CSRF Token**: Django가 CSRF 공격 방어에 사용하는 토큰
- **Context**: View에서 Template으로 전달하는 데이터
- **render()**: Template과 Context를 이용해 HTTP 응답 생성

## 테스트 및 검증
- `python manage.py check` 실행
- `python manage.py test todo -v 2` 실행
- Django 자동화 테스트 5개 통과
  - 기본 페이지 HTTP 200 응답
  - 기본 페이지 HTML 내용 확인
  - GET 입력값 출력 확인
  - POST 입력값 출력 확인
  - CSRF 토큰이 없는 POST 요청의 HTTP 403 응답 확인

## 전력 ICT TA 학습
- HTTP 요청·응답 구조와 GET/POST의 역할 이해
- HTTP 상태 코드 200, 403의 의미 확인
- CSRF 검증을 통한 웹 애플리케이션 보안 이해
- 자동화 테스트를 통한 변경 후 회귀 검증 학습
- Git Branch, Commit, Push, Pull Request, Merge를 통한 변경 이력 관리
- 향후 CI/CD, GCP, Kubernetes 배포 프로세스와 연계 예정

## Git Commit 및 PR
- 기능 브랜치: `feature/todo-form`
- 기능 커밋: `day004 feat: implement todo GET POST form and tests`
- GitHub Pull Request 생성 및 `main` 브랜치 병합 완료
- 로컬 `main` 브랜치 동기화 완료

## 다음 목표
- Django Model과 ORM 기초 학습
- Todo 데이터베이스 저장 구조 설계
- Todo 생성 및 목록 조회 기능 구현
- 데이터 저장·조회 흐름을 전력 ICT TA 관점에서 이해