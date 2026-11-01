from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
]

#<ind:todo_id>/toggle/ 어떤 URL에 대응하는가?
#views.toggle_todo 어떤 View 함수를 호출할 것인가?
#name='toggle_todo' 이 URL을 어떤 이름을 참조할 것인가?