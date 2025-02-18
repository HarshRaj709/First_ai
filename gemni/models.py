from django.db import models
from django.contrib.auth.models import User

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visitor_type = models.CharField(max_length=20)
    interest = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    budget = models.CharField(max_length=20)
    transport = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    ai_suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} - {self.visitor_type} ({self.created_at})"
