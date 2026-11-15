from django.test import Client
from django.urls import reverse
from todo.models import Todo
from datetime import date

client = Client(HTTP_HOST='localhost')
dated_todo = Todo.objects.create(
    title='날짜 렌더링 검증',
    scheduled_date=date(2026, 11, 10)
)
undated_todo = Todo.objects.create(
    title='날짜 미지정 검증'
)
response = client.get(reverse('index'))

print(response.status_code)
print('예정일: 2026-11-10' in response.content.decode())
print('예정일: 미지정' in response.content.decode())

dated_todo.delete()
undated_todo.delete()