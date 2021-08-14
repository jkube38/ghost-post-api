from django.db import models
from django.utils import timezone


# Create your models here.
class Posts(models.Model):
    broast = (
        (True, 'Boast'),
        (False, 'Roast')
    )

    boast_or_roast = models.BooleanField(null=True, choices=broast)
    text = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_time = models.DateTimeField(default=timezone.now)
    secret_key = models.CharField(max_length=6)

    def __str__(self):
        return self.text
