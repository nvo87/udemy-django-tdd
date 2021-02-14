from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_by_email(self):
        email = 'nvo87@yandex.ru'
        password = '12345asdASD'

        user = get_user_model()
        user.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
