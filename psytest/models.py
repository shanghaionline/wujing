from django.db import models

# Create your models here.
class Paper(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Question(models.Model):
    paper = models.ForeignKey(Paper)
    text = models.TextField()
    order = models.IntegerField(default = 0)

    def __str__(self):
        return self.text
    

class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    score = models.IntegerField(default = 0)
    show_result = models.BooleanField(default = False)
    next_question = models.ForeignKey(
        Question, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.text

class Result(models.Model):
    paper = models.ForeignKey(Paper)
    text = models.TextField()
    score_begin = models.IntegerField(default = 0)
    score_end = models.IntegerField(default = 0)

    def __str__(self):
        return self.text
    
