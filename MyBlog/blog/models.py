from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    mini_description = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title