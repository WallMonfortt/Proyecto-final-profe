from turtle import ondrag
from django.db import models
from tags.models import Tag
from users.models import User

class Newsletter(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    target = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='tags')
    author = models.ForeignKey(
        User, related_name='newsletters', on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name='members')
    voters = models.ManyToManyField(User, related_name='voters')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
