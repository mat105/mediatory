from django.contrib.auth.models import User
from django.db import models


class Tale(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    # TODO: Migrate to another table
    genre = models.PositiveSmallIntegerField()
    min_age = models.PositiveSmallIntegerField(default=0)

    publish_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, related_name='tales', on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.id}: {self.title}'
