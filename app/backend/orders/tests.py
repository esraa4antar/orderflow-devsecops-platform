from django.test import TestCase
from django.apps import apps


class OrdersAppTest(TestCase):
    def test_orders_app_is_installed(self):
        self.assertTrue(apps.is_installed("orders"))
# Create your tests here.
