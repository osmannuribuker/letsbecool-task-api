from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from core.apps.app.models import Todo
from core.apps.services.serializers import TodoSerializer
from core.apps.authentication.models import User
import json
from rest_framework.test import APIClient

client = APIClient()

class GetAllTodoTestCase(TestCase):
    # Test for get all todo on API

    def setUp(self):
        user = User.objects.create(username="tester", password="secret")
        Todo.objects.create(title='Wash the car', description='With soap', completed=True, created_by=user)
        Todo.objects.create(title='Watch Bohemian Rhapsody movie', description='For Queen', created_by=user)

    def test_get_all_todo(self):
        response = client.get(reverse('api:get_all_todos'))
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetTodoTestCase(TestCase):
    # Test for get single todo on API

    def setUp(self):
        user = User.objects.create(username="tester", password="secret")
        client.force_authenticate(user=user)
        Todo.objects.create(title='Wash the car', description='With soap', completed=True, created_by=user)
        Todo.objects.create(title='Watch Bohemian Rhapsody movie', description='For Queen', created_by=user)

    def test_get_valid_todo(self):
        response = client.get(reverse('api:single_todo', kwargs={'pk':1}))
        todo = Todo.objects.get(id=1)
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_todo(self):
        response = client.get(reverse('api:single_todo', kwargs={'pk':17}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateTodoTestCase(TestCase):
    # Test for create todo on API

    def setUp(self):
        self.valid_payload = {
            'title': 'Wash the car',
            'description': 'With Soap'
        }
        self.invalid_payload_1 = {
            'title': 'Watch Bohemian Rhapsody movie',
        }
        self.invalid_payload_2 = {
            'description': 'For Queen'
        }
        self.invalid_payload_3 = {
            'title': 'Cem Karaca',
            'description': 'Listen to the song "Ay Karanlık"',
            'completed': 'Yep'
        }
        user = User.objects.create(username="tester", password="secret")
        client.force_authenticate(user=user)

    def test_create_valid_todo(self):
        response = client.post(
            reverse('api:create_todo'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo_1(self):
        response = client.post(
            reverse('api:create_todo'),
            data=json.dumps(self.invalid_payload_1),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_todo_2(self):
        response = client.post(
            reverse('api:create_todo'),
            data=json.dumps(self.invalid_payload_2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_todo_3(self):
        response = client.post(
            reverse('api:create_todo'),
            data=json.dumps(self.invalid_payload_3),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateTodoTestCase(TestCase):
    # Test for update todo on API

    def setUp(self):
        user = User.objects.create(username="tester", password="secret")
        client.force_authenticate(user=user)
        Todo.objects.create(title='Wash the car', description='With soap', completed=True, created_by=user)
        Todo.objects.create(title='Watch Bohemian Rhapsody movie', description='For Queen', created_by=user)
        self.valid_payload = {
            'title': 'Wash the car',
            'description': 'With Prill',
            'completed': False
        }
        self.invalid_payload_1 = {
            'complated': 'complated'
        }
        self.invalid_payload_2 = {
            'title': 'Watch Bohemian Rhapsody movie',
            'description': 'For Freddie Mercury',
            'completed': 'completed'
        }

    def test_valid_update_todo(self):
        response = client.put(
            reverse('api:single_todo', kwargs={'pk': 1}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_todo_1(self):
        response = client.put(
            reverse('api:single_todo', kwargs={'pk': 2}),
            data=json.dumps(self.invalid_payload_1),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_update_todo_2(self):
        response = client.put(
            reverse('api:single_todo', kwargs={'pk': 2}),
            data=json.dumps(self.invalid_payload_2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteTodoTestCase(TestCase):
    # Test for delete todo on API

    def setUp(self):
        user = User.objects.create(username="tester", password="secret")
        client.force_authenticate(user=user)
        Todo.objects.create(title='Wash the car', description='With soap', completed=True, created_by=user)
        Todo.objects.create(title='Watch Bohemian Rhapsody movie', description='For Queen', created_by=user)

    def test_valid_delete_todo(self):
        response = client.delete(reverse('api:single_todo', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_todo(self):
        response = client.delete(reverse('api:single_todo', kwargs={'pk':17}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)