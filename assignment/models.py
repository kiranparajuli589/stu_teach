from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from forum.models import Class


class Assignment(models.Model):
    status = models.IntegerField(default=1)
    student = models.ForeignKey(User, related_name="student", on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)


class Task(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=500)
    classs = models.ForeignKey(Class, related_name='task', on_delete=models.CASCADE)
    # A Task can have many assignements
    assignments = models.ManyToManyField(Assignment, related_name="assignments")
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    created_time = models.DateTimeField(editable=False, auto_now= True)
    modified_time = models.DateTimeField(null=True, blank=True)

    # This method is for updating created and modified times on Saving an object
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)
