from rest_framework import serializers
from blog.models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # nome do modelo
        fields = '__all__' # lista de campos