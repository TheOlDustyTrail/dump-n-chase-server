import json
from rest_framework import status
from rest_framework.test import APITestCase
from chaseapi.models import Comment
from rest_framework.authtoken.models import Token


class CommentTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['comments', 'tokens', 'users', 'jersey_posts', 'teams']

    def setUp(self):
        self.comment = Comment.objects.first()
        token = Token.objects.get(user=self.comment.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_comment(self):
        """
        Ensure we can create a new comment.
        """
        # Define the endpoint in the API to which
        url = "/comments"

        # Define the request body
        data = {
            "jersey": 1,
            "user": 1,
            "comment": "Clue"
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the comment was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["jersey"], 1)
        self.assertEqual(json_response["user"], 1)
        self.assertEqual(json_response["comment"], "Clue")

    def test_get_comment(self):
        """
        Ensure we can get an existing comment.
        """

        # Seed the database with a comment
        comment = Comment()
        comment.jersey_id = 1
        comment.user_id = 1
        comment.comment = "Monopoly"
        comment.save()

        # Initiate request and store response
        response = self.client.get(f"/comments/{comment.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the comment was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["jersey"], 1)
        self.assertEqual(json_response["user"], 1)
        self.assertEqual(json_response["comment"], "Monopoly")

    def test_delete_comment(self):
        """
        Ensure we can delete an existing comment.
        """
        # Create a new comment
        comment = Comment()
        comment.jersey_id = 2
        comment.user_id = 1
        comment.comment = "Monopoly"
        comment.save()  # Save the comment to the database

        # DELETE the comment you just created
        response = self.client.delete(f"/comments/{comment.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the comment again to verify you get a 404 response
        response = self.client.get(f"/comments/{comment.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
