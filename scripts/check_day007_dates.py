from todo.models import Todo

dated_todo = (
    Todo.objects
    .filter(title="Day007 날짜 테스트")
    .order_by("-id")
    .first()
)

print(
    "날짜 있는 Todo:",
    dated_todo.scheduled_date if dated_todo else "Todo 없음"
)

undated_todo = (
    Todo.objects
    .filter(title="Day007 날짜 없는 테스트")
    .order_by("-id")
    .first()
)

print(
    "날짜 없는 Todo:",
    undated_todo.scheduled_date if undated_todo else "Todo 없음"
)