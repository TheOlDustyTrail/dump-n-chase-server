
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chaseapi.models import JerseyPost


class JerseyPostView(ViewSet):

    def retrieve(self, request, pk):
        jerseyPost = JerseyPost.objects.get(pk=pk)
        serializer = JerseyPostSerializer(jerseyPost)
        return Response(serializer.data)

    def list(self, request):

        jerseyPost = JerseyPost.objects.all()
        serializer = JerseyPostSerializer(jerseyPost, many=True)
        return Response(serializer.data)


class JerseyPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = JerseyPost
        fields = ('id', 'photo', 'year', 'description', 'team', 'user')
