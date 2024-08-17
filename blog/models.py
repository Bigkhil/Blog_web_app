from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #we used default to make the default value the timezone.now function without executing the function
    author = models.ForeignKey(User, on_delete=models.CASCADE) #the on_delete=CASCADE will delete all the posts of the user if user is deleted

    def __str__(self):
        return self.title
