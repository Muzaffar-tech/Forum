from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Topic, Comment, Reply
from .serializers import TopicSerializer, CommentSerializer, ReplySerializer


class TopicListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user, topic=topic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        serializer = ReplySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user, comment=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
