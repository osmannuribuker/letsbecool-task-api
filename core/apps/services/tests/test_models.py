from django.test import TestCase
from core.apps.app.models import Todo
from core.apps.authentication.models import User

class TodoTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="tester", password="secret")
        Todo.objects.create(title='Wash the car', description='With soap', completed=True, created_by=user)
        Todo.objects.create(title='Watch Bohemian Rhapsody movie', description='For Queen',  created_by=user)

    def test_description_for_tasks(self):
        wash_task = Todo.objects.get(title='Wash the car')
        watch_task = Todo.objects.get(title='Watch Bohemian Rhapsody movie')
        self.assertEqual(wash_task.description, 'With soap')
        self.assertEqual(watch_task.description, 'For Queen')

    def test_completed_tasks(self):
        completed_tasks = Todo.objects.filter(completed=True).count()
        self.assertEqual(completed_tasks, 1)

    def test_what_is_task(self):
        task = Todo.objects.get(description='With soap')
        self.assertEqual(task.what_is_task(), 'Task is "Wash the car"')

