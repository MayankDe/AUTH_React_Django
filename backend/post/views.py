from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from .JWTAuthentication import CustomJWTAuthentication



class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes= [CustomJWTAuthentication]
    permission_classes = [AllowAny]



class PostListView(ListAPIView):   
    
    queryset = Post.objects.all()      #If want to reverse then eryset = Post.objects.all().order_by('-created_at')  
    serializer_class = PostSerializer
    authentication_classes= [JWTAuthentication]
    permission_classes = [AllowAny]