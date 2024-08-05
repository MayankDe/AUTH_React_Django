from django.db import models
from accounts.models import UserAccount
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    def created_at_in_ist(self):
        return self.created_at.astimezone(timezone.get_current_timezone()).strftime('%Y-%m-%d %H:%M:%S %Z')

    def updated_at_in_ist(self):
        return self.updated_at.astimezone(timezone.get_current_timezone()).strftime('%Y-%m-%d %H:%M:%S %Z')
