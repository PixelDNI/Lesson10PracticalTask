from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=70, null=True)
    surname = models.CharField(max_length=70, null=True)
    age = models.IntegerField(null=True)
    email_address = models.EmailField(null=True)
    password = models.CharField(max_length=32, null=True)
    self_description = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"

    def get_absolute_url(self):
        return reverse('show_the_user', kwargs={'pk': self.id})

