from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chaseapi.models import DumpUser


class DumpUserView(ViewSet):

    def retrieve(self, request, pk):
        team = DumpUser.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def list(self, request):

        teams = DumpUser.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = DumpUser
        fields = ('id', 'user')
        depth = 1
