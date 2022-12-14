
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chaseapi.models import JerseyPost, Team
from django.contrib.auth.models import User


class JerseyPostView(ViewSet):

    def retrieve(self, request, pk):
        try:
            jerseyPost = JerseyPost.objects.get(pk=pk)
            serializer = JerseyPostSerializer(jerseyPost)
            return Response(serializer.data)
        except JerseyPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        jerseyPost = JerseyPost.objects.all()

        if "team" in request.query_params:
            query_value = request.query_params['team']
            filter_jerseys = jerseyPost.filter(team_id=query_value)
            jerseyPost = filter_jerseys

        serializer = JerseyPostSerializer(jerseyPost, many=True)
        return Response(serializer.data)

    def create(self, request):

        team = Team.objects.get(pk=request.data["team"])
        user = User.objects.get(id=request.auth.user_id)

        jerseyPost = JerseyPost.objects.create(
            photo=request.data["photo"],
            year=request.data["year"],
            description=request.data["description"],
            team=team,
            creator=user
        )
        serializer = JerseyPostSerializer(jerseyPost)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a jersey

        Returns:
            Response -- Empty body with 204 status code
        """
        team = Team.objects.get(pk=request.data["team"])
        jerseyPost = JerseyPost.objects.get(pk=pk)
        jerseyPost.description = request.data["description"]
        jerseyPost.photo = request.data["photo"]
        jerseyPost.year = request.data["year"]
        jerseyPost.team = team
        jerseyPost.creator = User.objects.get(id=request.auth.user_id)
        jerseyPost.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        jerseyPost = JerseyPost.objects.get(pk=pk)
        jerseyPost.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class JerseyPostSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    team = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = JerseyPost
        fields = ('id', 'photo', 'year', 'description', 'team', 'creator')
        depth = 1
