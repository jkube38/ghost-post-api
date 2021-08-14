# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ghost2app.models import Posts
from ghostapi.serializers import PostSerializer


# Create your views here.
class PostsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    @action(detail=False)
    def boasts(self, request):
        boasts = Posts.objects.filter(boast_or_roast=True)

        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roasts = Posts.objects.filter(boast_or_roast=False)

        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def sorted(self, request):
        sortedPosts = Posts.objects.all()

        def score(x):
            return x.likes - x.dislikes
        by_score = sorted(sortedPosts, key=score, reverse=True)

        serializer = self.get_serializer(by_score, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post.likes += 1
            post.save()
            return Response({'status': 'upvoted'})
        else:
            return Response(serializer.errors)

    @action(detail=True, methods=['put'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post.dislikes += 1
            post.save()
            return Response({'status': 'upvoted'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_Bad_Request)
