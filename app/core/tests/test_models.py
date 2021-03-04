from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_by_email(self):
        """ Test user creation with custom model using the email. """
        email = 'nvo87@yandex.ru'
        password = '12345asdASD'

        user = get_user_model()
        user = user.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """ Test normalization of the email. """
        email = 'nvo87@YANDEX.ru'
        password = '12345asdASD'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        """ Test email validation raises an error. """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123password')
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('nvo87', '123password')

    def test_create_superuser(self):
        """ Test creating user with staff and superuser settings. """
        user = get_user_model().objects.create_superuser(
            email='nvo87@YANDEX.ru',
            password='12345asdASD'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
