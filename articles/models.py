from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import TextInput


class Article(models.Model):
    occasions = (
        ('birthday', u'birthday'),
        ('anniversary', u'anniversary'),
        ('sympathy', u'sympathy'),
        ('graduation', u'graduation'),
        ('getwell', u'getwell'),
    )
    types = (
        ('1', u'bouqet'),
        ('2', u'plant'),
        ('2', u'flower'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    occasion = models.CharField(max_length=32, choices=occasions, null=True, blank=True)
    type = models.CharField(max_length=32, choices=types, null=True, blank=True)
    price = models.IntegerField(default=0,
        validators=[
            MinValueValidator(0),  # Optional: Specify minimum allowed value
            MaxValueValidator(999),  # Optional: Specify maximum allowed value
        ]
    )
    def __str__(self):
        if self.occasion:
            return f"{self.title} - {self.occasion}"
        return self.title


    def snippet(self):
        return self.body[:50]+"..."
