from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Blog
from .serializer import BlogSerializer
from django.shortcuts import get_object_or_404

# Get All Blogs
@api_view(['GET'])
@permission_classes([AllowAny])
def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

# Get Single Blog
@api_view(['GET'])
@permission_classes([AllowAny])
def get_single_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

# Create Blog
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data)
    
    return Response(serializer.errors)

# Update Blog
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        return Response({"error": "Not allowed"}, status=403)
    
    serializer = BlogSerializer(blog, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)

# Delete Blog
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        return Response({"error": "Not allowed"}, status=403)
    
    blog.delete()
    return Response({"message": "Blog Deleted Successfully"})