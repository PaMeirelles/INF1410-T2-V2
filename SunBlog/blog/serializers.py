from rest_framework import serializers
from blog.models import Post
class MTCarsSerializer(serializers.ModelSerializer):
    class Meta:
    model = Post # nome do modelo
    fields = '__all__' # lista de campos