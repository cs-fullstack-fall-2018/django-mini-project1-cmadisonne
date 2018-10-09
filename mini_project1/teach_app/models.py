from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    hours = models.IntegerField()
    work_date = models.DateTimeField(
        blank=True, null=True)
    entry_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.work_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
