import json
from rest_framework import status
from rest_framework.test import APITestCase
from chaseapi.models import JerseyPost
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from chaseapi.models import Team


class JerseyPostTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['tokens', 'users', 'jersey_posts', 'teams', 'likes']

    def setUp(self):
        self.jerseyPosts = JerseyPost.objects.first()
        token = Token.objects.get(user=self.jerseyPosts.creator)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_jerseyPost(self):
        """
        Ensure we can create a new jerseyPost.
        """
        # Define the endpoint in the API to which
        url = "/jerseyPosts"

        # Define the request body
        data = {
            "creator": [1],
            "photo": "URL(fdsafdsa)",
            "year": "2023",
            "description": "New cool jersey",
            "team": 3
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the jerseyPost was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["creator"], 1)
        self.assertEqual(json_response["photo"], "URL(fdsafdsa)")
        self.assertEqual(json_response["year"], "2023")
        self.assertEqual(json_response["description"], "New cool jersey")
        self.assertEqual(json_response["team"], 3)

    def test_get_jerseyPost(self):
        """
        Ensure we can get an existing jerseyPost.
        """

        # Seed the database with a jerseyPost
        jerseyPosts = JerseyPost()
        jerseyPosts.creator = User.objects.get(pk=1)
        jerseyPosts.photo = "URL(fdsafdsa)"
        jerseyPosts.year = "2023"
        jerseyPosts.description = "New cool jersey"
        jerseyPosts.team = Team.objects.get(pk=3)
        jerseyPosts.save()

        # Initiate request and store response
        response = self.client.get(f"/jerseyPosts/{jerseyPosts.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the jerseyPost was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["creator"], jerseyPosts.creator.id)
        self.assertEqual(json_response["photo"], "URL(fdsafdsa)")
        self.assertEqual(json_response["year"], "2023")
        self.assertEqual(json_response["description"], "New cool jersey")
        self.assertEqual(json_response["team"], jerseyPosts.team.id)

    def test_delete_jerseyPost(self):
        """
        Ensure we can delete an existing jerseyPost.
        """
        # Create a new jerseyPost
        jerseyPosts = JerseyPost()
        jerseyPosts.creator = User.objects.get(pk=1)
        jerseyPosts.photo = "URL(fdsafdsa)"
        jerseyPosts.year = "2023"
        jerseyPosts.description = "New cool jersey"
        jerseyPosts.team = Team.objects.get(pk=3)
        jerseyPosts.save()

        # DELETE the jerseyPost you just created
        response = self.client.delete(f"/jerseyPosts/{jerseyPosts.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the jerseyPost again to verify you get a 404 response
        response = self.client.get(f"/jerseyPosts/{jerseyPosts.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
