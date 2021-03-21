from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='nvo87@yandex.ru',
            password='12345asdASD'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='test1@yandex.ru',
            password='12345asdASD',
            name='Test user 1'
        )

    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)