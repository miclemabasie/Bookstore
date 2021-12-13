import decimal
from django.test import TestCase
from django.urls import reverse
from decimal import Decimal

from django.urls.base import resolve
from core import models

class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')

    def test_about_us_page_works(self):
        response = self.client.get(reverse('core:about'))
        self.assertContains(response, 'BookTime')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        

    def test_products_page_returns_active(self):
        models.Product.objects.create(
            name='The cathedral and the bazaar',
            slug = 'cathedral-bazaar',
            price=Decimal("2.00")
        )
        models.Product.objects.create(
            name='A tale of two cities',
            slug = 'tale-two-cities',
            price=Decimal("2.00"),
            active = False
        )

        response = self.client.get(reverse('core:product_list', kwargs={'tag': 'all'}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BookTime')

        product_list = models.Product.objects.active().order_by(
            'name'
        )

        self.assertEqual(list(response.context['object_list']), list(product_list))

    def test_products_page_filters_by_tags_and_active(self):
        cb = models.Product.objects.create(
            name='The cathedral and the bazaar',
            slug='cathedral-bazaar',
            price=Decimal('2.00')
        )

        cb.tags.create(name="Open source", slug='opensource')
        models.Product.objects.create(
            name='Microsoft Windows guide',
            slug='microsoft-windows-guide',
            price=Decimal('2.00')
        )

        response = self.client.get(
                reverse('core:product_list', kwargs={'tag': 'opensource'})
            )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BookTime')

        product_list = (
            models.Product.objects.active().filter(
                tags__slug='opensource'
            ).order_by('name')
        )

        self.assertEqual(list(response.context['object_list']), list(product_list))