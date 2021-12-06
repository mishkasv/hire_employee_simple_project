from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    work_experience = models.JSONField()
    total_experience = models.IntegerField(default=0)
    month_remainder = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
