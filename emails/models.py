from django.db import models

# Create your models here.
class Email(models.Model):
    fromm = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255, blank=False, null=False)
    body = models.CharField(max_length = 300)
    sentAt = models.DateField(auto_now=True)
    archived = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.fromm

