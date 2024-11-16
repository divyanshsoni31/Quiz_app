from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class question(models.Model):
    question=models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()