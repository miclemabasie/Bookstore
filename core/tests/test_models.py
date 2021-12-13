from unittest.case import TestCase
from django.test import testcases
from core import models
from decimal import Decimal


class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name='The cathedral and the bazzar',
            price = Decimal('19.00')
        )
        models.Product.objects.create(
            name='Pride and Prejudice',
            price = Decimal('19.00')
        )
        models.Product.objects.create(
            name='The  and the bazzar',
            price = Decimal('10.00'),
            active=False
        )

        self.assertEqual(len(models.Product.objects.active()), 2)