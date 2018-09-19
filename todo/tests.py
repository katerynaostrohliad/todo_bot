from django import setup
from django.test import TestCase
from .views import get_user
from .models import User
from django.test import Client


# Create your tests here.
class Tests(TestCase):
    @staticmethod
    def SetUp(self):
        setup()

    def test_insert_todo(self):
        data = {
            'tasks': 'buy milk',
            'reporter': 'Kate Ostrohliad'
        }
        response = self.client.post("/todo/", data)
        self.assertEqual((response.status_code, 201))

    def test_get_task_with_user(self):

        pass

    def test_get_one_todo(self):
        pass

    def test_delete_todo(self):
        user = User.objects.get(last_name=Ostrohliad)

        pass

