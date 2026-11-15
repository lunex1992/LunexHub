from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from datetime import date

from .models import Todo

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        scheduled_date_str = request.POST.get('scheduled_date', '').strip()

        scheduled_date = None
        valid_date = True

        if scheduled_date_str:
            try:
                scheduled_date = date.fromisoformat(scheduled_date_str)
            except ValueError:
                valid_date = False
        #date.fromisoformat()은 ISO 형식의 날짜 문자열을 Python date 객체로 변환합니다.
        
        if title and len(title) <= 200 and valid_date:
            Todo.objects.create(
                title=title,
                scheduled_date=scheduled_date
            )

        return redirect('index')

    todos = Todo.objects.all().order_by('-created_at', '-id')

    context = {
        'username': 'Lunex',
        'todos': todos,
        'todo_count': todos.count(),
    }

    return render(request, 'todo/index.html', context)

@require_POST
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.is_completed = not todo.is_completed
    todo.save(update_fields=['is_completed'])

    return redirect('index')


@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.delete()

    return redirect('index')


@require_POST
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    new_title = request.POST.get('title', '').strip()

    if new_title and len(new_title) <= 200:
        todo.title = new_title
        todo.save(update_fields=['title'])

    return redirect('index')