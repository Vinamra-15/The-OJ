from django.db import models

# Create your models here.

class Problem(models.Model):

    DIFFIULTY = (
        (0, 'EASY'),
        (1, 'MEDIUM'),
        (2, 'HARD')
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    difficulty = models.IntegerField(choices=DIFFIULTY, default=0)
    input = models.TextField(default='', help_text='Input format')
    output = models.TextField(default='', help_text='Expected output format')
    time_limit = models.IntegerField(default=1000, help_text='in milliseconds')
    

    def __str__(self):
        return self.name