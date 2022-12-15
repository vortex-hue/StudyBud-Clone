from django.db import models

# importing users for contrib.auth
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

#Topic class
class Topic(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    #ORDERING BY THE LATEST FIRST
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

#model for the message
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:60]

    class Meta:
        ordering = ['-updated', '-created']

#personal token types
# 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