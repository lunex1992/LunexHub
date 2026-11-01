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

## Day 006 — Django CRUD 완성 (Update & Delete)

### 1. 학습 목표 (Learning Objectives)

Day 005에서 구현한 Todo 생성(Create)과 조회(Read) 기능을 확장하여 수정(Update) 및 삭제(Delete)를 구현했다.

이번 학습의 목표는 다음과 같다.

- Django ORM을 이용한 데이터 수정 및 삭제
- URL Routing과 HTTP Method의 관계 이해
- HTML Form을 이용한 POST 요청 처리
- CSRF 보호 및 HTTP 상태 코드 이해
- 자동화 테스트를 통한 CRUD 기능 검증
- GitHub Pull Request 기반 형상관리

### 2. CRUD 기능 구현

CRUD는 데이터베이스에서 수행하는 네 가지 기본 작업을 의미한다.

| 구분 | 기능 | Django ORM |
|---|---|---|
| Create | Todo 생성 | `Todo.objects.create()` |
| Read | Todo 조회 | `Todo.objects.all()` |
| Update | Todo 수정 | `todo.save()` |
| Delete | Todo 삭제 | `todo.delete()` |

Day 006에서는 Update와 Delete 기능을 추가하여 LunexHub의 기본 CRUD를 완성했다.

### 3. Todo 완료 상태 변경 (Update)

**수정 파일:** `todo/views.py`

```python
@require_POST
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.is_completed = not todo.is_completed
    todo.save(update_fields=['is_completed'])

    return redirect('index')
```

**핵심 학습 내용**

- `@require_POST`: POST 요청만 허용
- `get_object_or_404()`: Todo 조회 및 존재하지 않는 객체에 대한 404 처리
- `not`: 완료 상태를 `True`와 `False` 사이에서 전환
- `save(update_fields=['is_completed'])`: 완료 상태 필드만 DB에 저장
- `redirect('index')`: 작업 후 Todo 목록으로 이동

완료 버튼을 누르면 미완료 상태가 완료로 변경되고, 완료 취소 버튼을 누르면 다시 미완료 상태가 된다.

### 4. Todo 삭제 기능 (Delete)

**수정 파일:** `todo/views.py`

```python
@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.delete()

    return redirect('index')
```

**핵심 학습 내용**

- `delete()`: Django ORM을 이용한 데이터 삭제
- `get_object_or_404()`: 삭제 대상이 존재하지 않으면 HTTP 404 반환
- `@require_POST`: GET 요청으로 삭제되지 않도록 제한
- `redirect()`: 삭제 후 목록 페이지로 이동

이번에 구현한 방식은 실제 DB 레코드를 삭제하는 Hard Delete 방식이다.

향후 복구 및 감사 기록이 필요한 경우 Soft Delete 방식도 고려할 수 있다.

### 5. URL Routing과 HTTP Method

**수정 파일:** `todo/urls.py`

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
]
```

URL Routing은 요청 경로와 View 함수를 연결한다.

HTTP Method는 요청을 보내는 Client가 결정하며, URL 자체가 GET 또는 POST를 결정하는 것은 아니다.

| 요청 | 처리 결과 |
|---|---|
| `POST /todo/5/toggle/` | Todo 상태 변경 후 302 Redirect |
| `GET /todo/5/toggle/` | 405 Method Not Allowed |
| `POST /todo/5/delete/` | Todo 삭제 후 302 Redirect |
| `GET /todo/5/delete/` | 405 Method Not Allowed |
| 존재하지 않는 Todo에 POST | 404 Not Found |

데이터를 변경하는 작업은 POST로 처리하고, GET 요청은 조회 목적으로 사용하도록 설계했다.

### 6. HTML Form 및 CSRF 보호

**수정 파일:** `todo/templates/todo/index.html`

완료 상태 변경과 삭제 기능을 HTML Form으로 연결했다.

**완료 상태 변경 Form**

```html
<form action="{% url 'toggle_todo' todo.id %}" method="post">
    {% csrf_token %}
    <button type="submit">완료 상태 변경</button>
</form>
```

**삭제 Form**

```html
<form action="{% url 'delete_todo' todo.id %}" method="post">
    {% csrf_token %}
    <button type="submit">삭제</button>
</form>
```

**핵심 학습 내용**

- `action`: HTTP 요청을 보낼 URL
- `method="post"`: POST 방식으로 요청
- `{% url %}`: Django URL 이름을 실제 URL로 변환
- `{% csrf_token %}`: CSRF 공격 방어를 위한 Token 삽입
- `<button type="submit">`: Form 제출

브라우저의 개발자 도구(Network 탭)에서 POST 요청과 HTTP 302 Redirect를 직접 확인했다.

### 7. Django Test Client와 ALLOWED_HOSTS

Django Shell에서 테스트 Client를 사용할 때 다음 오류가 발생했다.

```text
DisallowedHost: Invalid HTTP_HOST header: 'testserver'
```

Django Test Client는 기본적으로 `testserver`라는 Host를 사용한다.

현재 프로젝트 설정에서는 해당 Host가 허용되지 않아 오류가 발생했다.

Shell 실습에서는 다음과 같이 해결했다.

```python
client = Client(HTTP_HOST='localhost')
```

**학습 결과**

- `HTTP_HOST`: HTTP 요청에 포함된 Host 정보
- `ALLOWED_HOSTS`: Django에서 허용하는 Host 이름 목록
- `DisallowedHost`: 허용되지 않은 Host 요청에 대한 예외
- `python manage.py test`: 일반적으로 테스트 환경에서 `testserver` 사용 가능

`ALLOWED_HOSTS`는 네트워크 방화벽이 아니라 HTTP Host 검증을 위한 애플리케이션 보안 설정이다.

### 8. 자동화 테스트 (Automated Testing)

**수정 파일:** `todo/tests.py`

기존 Day 005 테스트 8개에 신규 테스트 8개를 추가했다.

| 구분 | 테스트 내용 |
|---|---|
| Update 1 | POST 요청으로 완료 상태 변경 |
| Update 2 | 완료 상태를 다시 미완료로 변경 |
| Update 3 | GET 요청 차단 및 DB 상태 유지 |
| Update 4 | 존재하지 않는 Todo 수정 시 404 |
| Delete 1 | POST 요청으로 Todo 삭제 |
| Delete 2 | GET 요청 차단 및 DB 데이터 유지 |
| Delete 3 | 존재하지 않는 Todo 삭제 시 404 |
| Delete 4 | CSRF Token 없는 삭제 요청 시 403 |

**테스트 실행 명령어**

```bash
python manage.py test todo -v 2
```

**실행 결과**

```text
Ran 16 tests in 0.xxxs

OK
```

기존 테스트와 신규 테스트를 포함하여 총 16개가 통과했다.

이러한 테스트는 새로운 기능을 추가하면서 기존 기능이 손상되지 않았는지 확인하는 Regression Test(회귀 테스트)의 기반이 된다.

### 9. Git & GitHub 형상관리

이번 Day 006에서는 기능 개발과 문서 작업을 브랜치로 분리했다.

**기능 개발 브랜치**

```text
feature/todo-crud
```

**주요 작업**

1. Django CRUD Update/Delete 기능 구현
2. 자동화 테스트 16개 통과
3. Git Commit 및 GitHub Push
4. Pull Request 생성 및 코드 변경사항 검토
5. `main` 브랜치에 Merge
6. 로컬 `main` 동기화 및 테스트 재실행

**로컬 동기화 명령어**

```bash
git switch main
git pull --ff-only origin main
```

`--ff-only`를 이용해 불필요한 Merge Commit 생성 없이 동기화했다.

### 10. 전력 ICT Technical Architect 관점

이번 학습을 통해 다음과 같은 실무 개념을 익혔다.

| 기술 개념 | TA 관점 |
|---|---|
| HTTP Method | 조회와 상태 변경 요청 분리 |
| URL Routing | 요청 경로와 처리 기능의 연결 |
| Django ORM | 애플리케이션과 DB 간 데이터 처리 |
| CSRF | 웹 애플리케이션 보안 |
| HTTP 404 / 405 | 오류 및 요청 제한 처리 |
| Regression Test | 시스템 변경 후 기존 기능 검증 |
| Pull Request | 코드 리뷰 및 변경 관리 |
| Hard / Soft Delete | 데이터 보존 및 삭제 정책 |

향후 실제 운영 환경에서는 사용자 인증 및 권한 관리, 감사 로그, 데이터 백업, 장애 대응, 모니터링 등을 추가로 고려해야 한다.

### 11. Day 006 학습 결과

**완료한 기능**

- Todo 생성(Create)
- Todo 조회(Read)
- Todo 완료 상태 변경(Update)
- Todo 삭제(Delete)
- HTML Form과 Django View 연결
- POST 및 CSRF 기반 상태 변경 처리
- 자동화 테스트 총 16개 통과
- GitHub PR 및 Merge 완료

**핵심 성과**

Django Model, View, Template, URL Routing, ORM, SQLite를 연결하여 브라우저에서 사용할 수 있는 기본 Todo CRUD 애플리케이션을 완성했다.

### 12. Next Steps — Day 007 이후

- Todo 제목 수정 기능
- Todo 날짜 및 일정 관리 기능
- FullCalendar 기반 달력 UI
- MySQL 데이터베이스 도입
- Docker 컨테이너 환경 구축
- GCP 배포 및 운영
- Kubernetes(GKE) 기반 오케스트레이션

장기적으로 LunexHub를 전력 ICT Technical Architect 역량을 학습하는 실습 프로젝트로 발전시킬 예정이다.