from model_bakery import baker
from rest_framework import status

from library.models import Tale
from library.serializers import TaleSerializer
from library.tests.api.base import BaseTestCase


class TaleTestCase(BaseTestCase):

    def test_get_tales(self):
        baker.make(Tale, title='Test', owner=self.user)
        response = self.client.get('/tale/', format='json')
        tales = Tale.objects.all()
        serializer = TaleSerializer(tales, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data['results']

        self.assertEqual(len(results), len(tales))
        self.assertEqual(len(tales), 1)
        self.assertEqual(results, serializer.data)

    def test_get_tale(self):
        tale = baker.make(Tale, title='Test', owner=self.user)
        response = self.client.get(f'/tale/{tale.id}/', format='json')

        tale = Tale.objects.get(title='Test')
        serializer = TaleSerializer(tale)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_tale_throws_404_if_does_not_exists(self):
        total_tales = Tale.objects.all().count()

        response = self.client.get(f'/tale/{total_tales+1}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_tale(self):
        prev_tales_count = Tale.objects.all().count()

        self.login()
        tale = {
            'title': 'test_post_tale',
            'content': 'Test content',
            'genre': 1,
            'min_age': 4
        }

        response = self.client.post(f'/tale/', data=tale, format='json')

        tale = Tale.objects.get(title='test_post_tale')
        serializer = TaleSerializer(tale)

        new_tales_count = Tale.objects.all().count()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(new_tales_count, prev_tales_count + 1)

        self.assertEqual(response.data['owner'], self.user.username)

    def test_post_tale_throws_unauthorized_if_not_logged_in(self):
        tale = {
            'title': 'test_post_tale',
            'content': 'Test content',
            'genre': 1,
            'min_age': 4
        }

        response = self.client.post(f'/tale/', data=tale, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
