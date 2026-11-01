from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Todo

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()


        if title:
            Todo.objects.create(title=title)

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