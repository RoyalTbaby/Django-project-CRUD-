from django.db import models


class User(models.Model):
    jobs = (
        ('Backend Developer', 'BACKEND DEVELOPER'),
        ('IT-Admin', 'IT-ADMIN'),
        ('Sales Representative', 'SALES REPRESENTATIVE'),
        ('Support', 'SUPPORT'),
        ('DevOps Engineer', 'DEVOPS ENGINEER'),
        ('Frontend developer', 'FRONTEND DEVELOPER'),
        ('Human Resources', 'HUMAN RESOURCES')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profession = models.CharField(max_length=100, choices=jobs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
