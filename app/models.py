from django.db import models

# Create your models here.
class Post(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title