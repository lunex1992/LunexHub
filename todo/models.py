from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Day 007: Todo 예정 날짜
    scheduled_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title