
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chaseapi.models import Like, JerseyPost
from django.contrib.auth.models import User


class LikeView(ViewSet):

    def retrieve(self, request, pk):
        like = Like.objects.get(pk=pk)
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    def list(self, request):

        like = Like.objects.all()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)

    def create(self, request):

        jersey = JerseyPost.objects.get(pk=request.data["jersey"])
        user = User.objects.get(id=request.auth.user_id)

        like = Like.objects.create(
            jersey=jersey,
            user=user

        )
        serializer = LikeSerializer(like)
        return Response(serializer.data)

    def destroy(self, request, pk):
        like = Like.objects.get(pk=pk)
        like.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'jersey', 'user')
