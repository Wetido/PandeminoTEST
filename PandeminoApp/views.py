from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from PandeminoApp.serializers import *
from PandeminoApp.models import BlogPost

from rest_framework import generics


@api_view(['GET'])
def api_detail_all(request):

    blog_posts = BlogPost.objects.all()
    if request.method == "GET":
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_detail_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data)

        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["faliture"] = "delete falied"
        return Response(data=data)


@api_view(['POST'])
def api_create_view(request):


    blog_post = BlogPost(title=request.data)

    if request.method == "POST":
        serializer = serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
