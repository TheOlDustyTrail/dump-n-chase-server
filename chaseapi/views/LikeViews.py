
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chaseapi.models import Like


class LikeView(ViewSet):

    def retrieve(self, request, pk):
        like = Like.objects.get(pk=pk)
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    def list(self, request):

        like = Like.objects.all()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'jersey', 'user')
