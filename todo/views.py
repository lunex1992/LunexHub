from django.shortcuts import render, redirect
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