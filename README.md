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

## Day 005 — Django Model, ORM 및 데이터베이스 영속성

### 1. 학습 목표 (Learning Objectives)

- 관계형 데이터베이스(RDBMS)의 기본 개념 이해
- Django Model을 이용한 데이터 구조 정의
- Migration을 이용한 데이터베이스 스키마 관리
- Django ORM을 활용한 데이터 생성 및 조회
- Django View와 SQLite 데이터베이스 연결
- POST-Redirect-GET(PRG) 패턴 적용
- Django 자동화 테스트 작성 및 검증
- Git 및 GitHub를 이용한 형상관리

### 2. Django Model 설계

**파일:** `todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

**Model 필드 구성**

| 필드 | 데이터 타입 | 설명 |
|---|---|---|
| `id` | 자동 생성 PK | Todo 고유 식별자 |
| `title` | CharField | 할 일 제목, 최대 200자 |
| `is_completed` | BooleanField | 완료 여부, 기본값 False |
| `created_at` | DateTimeField | 최초 생성 시각 자동 기록 |

**핵심 개념**

- `Model`: 데이터베이스 테이블의 구조를 Python 클래스로 정의
- `Primary Key(PK)`: 각 데이터를 고유하게 식별하는 값
- `Field`: 데이터베이스 테이블의 컬럼에 대응하는 Model 속성

### 3. Database Migration

Model 변경사항을 실제 SQLite 데이터베이스에 반영했다.

**실행 명령어**

```bash
python manage.py makemigrations todo
python manage.py sqlmigrate todo 0001
python manage.py migrate
python manage.py showmigrations todo
```

**명령어별 역할**

| 명령어 | 설명 |
|---|---|
| `makemigrations` | Model 변경사항을 Migration 파일로 생성 |
| `sqlmigrate` | Migration에 해당하는 SQL 확인 |
| `migrate` | Migration을 실제 DB에 적용 |
| `showmigrations` | Migration 적용 상태 확인 |

**실습 결과**

- `todo/migrations/0001_initial.py` 생성
- SQLite에 `todo_todo` 테이블 생성
- `[X] 0001_initial` 확인

**배운 점:** `makemigrations`는 변경 작업을 정의하고, `migrate`는 해당 변경사항을 실제 데이터베이스에 적용한다.

### 4. Django ORM 실습

Django Shell에서 ORM을 이용해 Todo 데이터를 생성하고 조회했다.

```python
from todo.models import Todo

# Todo 생성
Todo.objects.create(title='Django ORM 공부하기')
Todo.objects.create(title='전력 ICT TA 공부하기')

# 전체 조회
Todo.objects.all()

# 개수 조회
Todo.objects.count()

# 미완료 Todo 조회
Todo.objects.filter(is_completed=False)
```

**핵심 개념**

- `ORM(Object-Relational Mapping)`: Python 객체를 통해 데이터베이스를 조작하는 기술
- `QuerySet`: Django에서 데이터 조회를 표현하는 객체
- `objects.create()`: 데이터 생성 및 저장
- `objects.all()`: 전체 데이터 조회
- `objects.filter()`: 조건에 맞는 데이터 조회
- `objects.count()`: 데이터 개수 조회
- `Persistence(영속성)`: 프로그램 종료 후에도 저장된 데이터가 유지되는 특성

**실습 결과:** Django Shell을 종료하고 다시 실행해도 SQLite에 저장한 Todo가 유지됨을 확인했다.

### 5. View와 데이터베이스 연결

**파일:** `todo/views.py`

Django View에서 HTTP POST 요청을 받아 Todo를 저장하고, GET 요청에서 저장된 목록을 조회하도록 구현했다.

**주요 구현 내용**

- `request.POST`로 Todo 제목 수신
- `.strip()`으로 입력값의 앞뒤 공백 제거
- `Todo.objects.create()`로 SQLite에 저장
- `Todo.objects.all().order_by()`로 목록 조회
- `render()`를 이용한 HTML 출력
- `redirect()`를 이용한 PRG 패턴 적용

**HTTP 요청 처리 흐름**

```text
[Browser]
    |
    | HTTP POST
    v
[Django View]
    |
    | ORM Create
    v
[SQLite Database]
    |
    | HTTP 302 Redirect
    v
[Browser]
    |
    | HTTP GET
    v
[Django View]
    |
    | ORM Query
    v
[HTML Template]
```

**PRG(Post-Redirect-Get) 패턴**

POST 요청으로 데이터를 저장한 후 Redirect를 통해 GET 요청으로 전환하는 방식이다.

일반적인 브라우저 새로고침으로 인한 중복 POST 제출을 줄일 수 있다.

### 6. 자동화 테스트 (Automated Testing)

**파일:** `todo/tests.py`

Django의 `TestCase`와 `Client`를 이용해 총 8개의 테스트를 작성했다.

| 번호 | 테스트 항목 | 검증 내용 |
|---|---|---|
| 1 | HTTP GET | 정상 응답 200 |
| 2 | HTML Content | 기본 화면 내용 출력 |
| 3 | GET 요청 | Todo가 생성되지 않음 |
| 4 | POST 요청 | Todo 저장 및 302 Redirect |
| 5 | CSRF | 토큰 없는 POST 요청 403 차단 |
| 6 | Blank Input | 공백 입력 시 저장하지 않음 |
| 7 | Todo List | 저장된 Todo 목록 출력 |
| 8 | Ordering | 최신 Todo 우선 정렬 |

**테스트 실행**

```bash
python manage.py check
python manage.py test todo -v 2
```

**테스트 결과**

```text
Ran 8 tests
OK
```

**배운 점:** 자동화 테스트는 기능 변경 후 기존 동작이 정상적으로 유지되는지 검증하는 회귀 테스트(Regression Testing)에 활용할 수 있다.

### 7. Git 및 GitHub 형상관리

**작업 브랜치:** `feature/todo-model`

**진행 과정**

1. 기능 브랜치 생성 및 코드 작성
2. Django Model 및 Migration 구현
3. View, Template, Test 코드 수정
4. 자동화 테스트 8개 통과
5. Git Commit 및 GitHub Push
6. Pull Request 생성 및 변경사항 검토
7. `main` 브랜치 Merge
8. 로컬 `main` 동기화 및 테스트 재검증

**주요 Git 명령어**

```bash
git status
git diff
git add
git commit
git push
git switch main
git pull --ff-only origin main
```

### 8. 전력 ICT TA 관점의 학습

#### 8.1 Database Schema Management

데이터베이스 구조 변경 시 고려할 사항:

- 기존 데이터와의 호환성
- Migration 적용 순서
- 데이터 백업 및 복구 전략
- 서비스 중단 및 성능 영향
- 스키마 변경 이력 관리

#### 8.2 Three-Tier Architecture

| 계층 | LunexHub 구성 | 역할 |
|---|---|---|
| Presentation Tier | Browser, HTML | 사용자 화면 |
| Application Tier | Django View, ORM | 비즈니스 로직 및 요청 처리 |
| Data Tier | SQLite | 데이터 저장 및 조회 |

현재는 논리적으로 3개 계층을 구분하며, 향후 MySQL 및 GCP를 도입해 데이터베이스를 별도 서비스로 분리할 예정이다.

#### 8.3 Change Management

- Git Branch를 이용한 작업 분리
- Commit을 통한 변경 이력 관리
- Pull Request를 이용한 코드 검토
- 자동화 테스트를 통한 변경 영향 검증
- README를 통한 기술 문서화

### 9. Day 005 학습 결과

**구현 완료**

- Django Todo Model
- 초기 Database Migration
- ORM 기반 Todo 생성(Create)
- ORM 기반 Todo 조회(Read)
- SQLite 데이터 영속성
- POST-Redirect-GET 패턴
- 자동화 테스트 8개 통과
- GitHub PR 및 Merge

**핵심 성과:** 단순히 입력값을 화면에 출력하던 웹 애플리케이션을 실제 데이터베이스에 데이터를 저장하고 조회하는 구조로 발전시켰다.

### 10. 다음 학습 계획 (Day 006)

- Todo 수정(Update) 기능 구현
- Todo 삭제(Delete) 기능 구현
- Django ORM을 이용한 CRUD 완성
- 수정·삭제 기능 자동화 테스트 작성

**향후 기술 로드맵:** Django CRUD → FullCalendar → MySQL → Docker → GCP → Kubernetes(GKE)
