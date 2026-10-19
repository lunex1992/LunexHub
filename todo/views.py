from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'username': 'Lunex',
        'todo_count': 5,
    }

    return render(request, 'todo/index.html', context)
#render()는 지정한 템플릿에 데이터를 적용해 HTML을 생성하고, 그 결과를 HttpResponse 객체로 반환합니다.