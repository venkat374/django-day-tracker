from django.db import models

class Task(models.Model):
    DAYS_OF_WEEK = [
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    task_text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets on creation

    def __str__(self):
        return f"{self.day.capitalize()}: {self.task_text} ({'Done' if self.done else 'Pending'})"

    class Meta:
        ordering = ['created_at'] # Ensures tasks are always listed in the order they were added