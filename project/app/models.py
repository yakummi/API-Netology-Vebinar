from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    # id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    favourite_by = models.ManyToManyField(User, related_name="favourite_notes")
    is_private = models.BooleanField(default=True)


