from django.test import TestCase, Client
from core.models import Questions
from django.contrib.auth.models import User


class TestModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username = 'amin', 
            email='amin@yahoo.com', 
            password='amin'
        )
        self.question = Questions.objects.create(
            user = user,
            title = 'This is test question',
            body= 'this is test question body'
        )


    def test_question_create(self):
        self.assertEqual(self.question.slug, 'this-is-test-question')