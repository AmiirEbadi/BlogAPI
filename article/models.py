from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField

# Create your models here.

CHOICES = [
    ('P', 'Published'),
    ('D', 'Draft')
]

class Article(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,        
    )
    body = models.TextField(
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=20,
        choices=CHOICES,
    )
    is_special = models.BooleanField(
        blank=False,
    )

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title
