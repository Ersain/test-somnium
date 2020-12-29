from django.db import models
from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # date_joined = models.DateField(auto_now_add=True)

    position = models.ManyToManyField(to='Position')
    manager = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    title = models.CharField(max_length=255)
    parent_department = models.ForeignKey(to='Department', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'
