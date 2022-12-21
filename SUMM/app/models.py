from django.db import models
from django.urls import reverse

class User(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    QuotaLimit = models.IntegerField()
    QuotaSpent = models.IntegerField()

    def __str__(self):
        return self.Name
    
    #def get_absolute_url(self):
     #   return reverse('user_edit', kwargs={'pk': self.Id})

class Translation(models.Model):
    Id = models.IntegerField(primary_key=True)
    InputText = models.CharField(max_length=200)
    OutputText = models.CharField(max_length=200)
    FromUserId = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
    
    #def get_absolute_url(self):
     #   return reverse('translation_edit', kwargs={'pk': self.Id})
