from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=250, blank=True)
    PhoneNumber = models.CharField(max_length=250, blank=True)
    onApp = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contacts"
