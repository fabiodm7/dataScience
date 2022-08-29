from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """Modelo de postagem para o blog"""
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Representação em texto do modelo"""
        return self.text