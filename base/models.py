from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null= True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']



