from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response

def home(request):
    return render(request, 'blog/home.html')

class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.all().order_by('dt_publicado')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)