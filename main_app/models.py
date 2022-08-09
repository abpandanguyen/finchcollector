from smtplib import SMTPRecipientsRefused
from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    commonName = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    iocSequence = models.IntegerField()

    def __str__(self):
        return f'{self.commonName} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    location = models.CharField(max_length=50)

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']