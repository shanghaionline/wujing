from django.db import models

# Create your models here.
class Paper(models.Model):
    name = models.CharField('问卷名称', max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '心理测试问卷'
        verbose_name_plural = verbose_name


class Question(models.Model):
    paper = models.ForeignKey(Paper)
    text = models.TextField('问题题目')
    order = models.IntegerField('序号', default = 0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '心理测试题目'
        verbose_name_plural = verbose_name

    

class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField('选项内容')
    score = models.IntegerField('得分', default = 0)
    show_result = models.BooleanField('是否跳至结果', default = False)
    next_question = models.ForeignKey(
        Question, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.text

class Result(models.Model):
    paper = models.ForeignKey(Paper)
    text = models.TextField('结果内容')
    score_begin = models.IntegerField('分数范围(起始)', default = 0)
    score_end = models.IntegerField('分数范围(结束)', default = 0)

    def __str__(self):
        return self.text
    
