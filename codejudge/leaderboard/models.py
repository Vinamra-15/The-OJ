from django.db import models
from problem.models import Problem
from django.contrib.auth.models import User



class Submission(models.Model):

    VERDICT_CHOICES = (
        ('AC', 'accepted'),
        ('WA', 'wrong answer'),
        ('TLE', 'time limit exceeded'),
        ('CE', 'compile error'),
        ('RE', 'runtime error'),
        ('TEST', 'testing')
    )

    COMPILER_CHOICES = (('0','python'),('1','c++'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    submitted_code = models.TextField()
    submission_time = models.DateTimeField(auto_now_add=True)
    compiler = models.CharField(max_length=30, choices=COMPILER_CHOICES,default='python')
    verdict = models.CharField(max_length=4, choices=VERDICT_CHOICES, default='TEST')

    def __str__(self):
        return str(self.id)
