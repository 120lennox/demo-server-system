from rest_framework import serializers
from .models import Post

# serialzers here
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'image',
            'created_at',
        ]