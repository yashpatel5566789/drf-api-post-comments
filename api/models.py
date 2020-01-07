from django.db import models
import json

# Create your models here.
class PostQuerySet(models.QuerySet):
    pass

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)



class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return ({
            "title" : self.title,
            "id" : self.id,
        })
    class Meta:
            verbose_name='Post post'
            verbose_name_plural='Post posts'

class Comment(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    message = models.TextField(blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str({
            "title" : self.title,
            "message" : self.message,
            "id" : self.id,
        })

class PostId(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class CommentId(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    message = models.TextField(blank=True)
    post = models.ForeignKey(PostId, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str({
            "title" : self.title,
            "message" : self.message,
            "id" : self.id,
        })

data = {
    'title': 'The Grey Album',
    'description': 'The Grey Album description',
    'comments': [
        {
            'title': 'Public Service Announcement',
            'message': '1. comment message for post 3'
        },
        {
            'title': 'What More Can I Say',         
            'message': '2. comment message for post 3'
        },
        {
            'title': 'Encore',
            'message': '3. comment message for post 3'
        },
    ],
}

