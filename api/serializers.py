from rest_framework import serializers
from .models import Post, Comment, PostId,CommentId

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'message', 'id',]
        # fields = ['post', 'title', 'message', 'id', 'url']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id','title', 'description', "comments"]
        
class PostIdSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id','title', 'description']


class CommentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'message', 'id',]