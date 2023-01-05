import json
from rest_framework import status
from rest_framework.test import APITestCase
from chaseapi.models import Team
from rest_framework.authtoken.models import Token


class TeamTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['tokens', 'teams', 'users']

    def setUp(self):
        self.team = Team.objects.first()
        token = Token.objects.get(user=1)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_team(self):
        """
        Ensure we can get an existing team.
        """

        # Seed the database with a team
        team = Team()
        team.name = "Chiefs"
        team.bio = "Semi pro team from Charlston"
        team.logo = "fsdafdafdsa"
        team.carousel1 = "Photo 1"
        team.carousel2 = "Photo 2"
        team.carousel3 = "Photo 3"
        team.save()

        # Initiate request and store response
        response = self.client.get(f"/teams/{team.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the team was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["name"], "Chiefs")
        self.assertEqual(json_response["bio"], "Semi pro team from Charlston")
        self.assertEqual(json_response["logo"], "fsdafdafdsa")
        self.assertEqual(json_response["carousel1"], "Photo 1")
        self.assertEqual(json_response["carousel2"], "Photo 2")
        self.assertEqual(json_response["carousel3"], "Photo 3")
