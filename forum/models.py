from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_set')
    created_at = models.DateTimeField(auto_now_add=True)
    class_avatar = models.ImageField(upload_to='class_image', blank=True)
    students = models.ManyToManyField(User, related_name='class_student')

    def get_absolute_url(self):
        return reverse('forum:class_list')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    board = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='post_set')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    upvoted_by = models.ManyToManyField(User, related_name="post_upvoted")
    downvoted_by = models.ManyToManyField(User, related_name='post_downvoted')
    # tags = models.CharField(max_length=100)  # TODO
    # post_status = models.BooleanField(default=False)


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    upvoted_by = models.ManyToManyField(User, related_name='comment_upvoted')
    downvoted_by = models.ManyToManyField(User, related_name='comment_downvoted')


class Reply(models.Model):
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reply_set")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_set")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """Reaction todo"""  # TODO