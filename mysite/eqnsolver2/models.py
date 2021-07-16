from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=150)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text