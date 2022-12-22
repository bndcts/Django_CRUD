from django.db import models
from django.urls import reverse

class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    QuotaLimit = models.IntegerField()
    QuotaSpent = models.IntegerField()

    def __str__(self) -> str:
        return self.Name


class Translation(models.Model):
    Id = models.AutoField(primary_key=True)
    InputText = models.CharField(max_length=200)
    OutputText = models.CharField(max_length=200)
    FromUserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.Name