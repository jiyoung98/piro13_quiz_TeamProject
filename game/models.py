from django.db import models

# Create your models here.
class User(models.Model):
    quiz_title = models.CharField(max_length=50, default=0)
    name = models.CharField(max_length=30)
    quiz_url = models.URLField(max_length=200, null=True, blank=True, unique=True)
    answer = models.CharField(default="", max_length=10, null=True, blank=True)
    count = models.IntegerField(default="0")

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    opt1 = models.CharField(max_length=50)
    opt2 = models.CharField(max_length=50)
    opt3 = models.CharField(max_length=50)
    opt4 = models.CharField(max_length=50)
    opt5 = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+"번 문제"

class Challenger(models.Model):
    # user_obj = models.ForeignKey("User", on_delete=models.CASCADE)
    user_obj = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30)
    result = models.IntegerField(null=True, blank=True)
    answer = models.CharField(default="", max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-result', 'name']