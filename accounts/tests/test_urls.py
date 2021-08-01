from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import UserDashboard, UserRegister


class TestUrls(SimpleTestCase):
    def test_register(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegister)

    def test_dashboard(self):
        url = reverse('accounts:dashboard', args=['amin',])
        self.assertEqual(resolve(url).func.view_class, UserDashboard)
