import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class PyUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=32, blank=True, null=True)  # Store salt if needed
    ranking_points = models.IntegerField(default=0)
    id_hash = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique ID hash

    def __str__(self):
        return self.username

class Note(models.Model):
    user = models.ForeignKey(PyUser, on_delete=models.CASCADE, related_name="user_notes")  # Fix conflict
    module_name = models.CharField(max_length=255)
    section_name = models.CharField(max_length=255)
    content = models.TextField()
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.module_name} - {self.section_name}"

    def can_access(self, user):
        return self.user == user
    
    class Meta:
        ordering = ["position"]  # Order by position field
