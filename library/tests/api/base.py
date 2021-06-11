import base64

from django.contrib.auth.models import User

from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):

    def setUp(self):
        try:
            user = User.objects.get(username='testuser001')
        except User.DoesNotExist:
            user = User(
                email='test_user@test.com',
                username='testuser001',
            )
            user.set_password('test123321')
            user.save()

        self.user = user
        self.user_password = 'test123321'

    def login(self, user=None, password=None):
        if user is None:
            user = self.user
            password = self.user_password

        header = base64.b64encode(bytes(f'{user.username}:{password}', 'utf8')).decode('utf8')
        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + header)
