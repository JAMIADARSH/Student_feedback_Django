from django.db import models


class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()
    rating = models.IntegerField(choices=[
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent')
    ])

    def __str__(self):
        return self.student_name


# Create your models here.
