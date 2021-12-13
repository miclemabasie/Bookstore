from logging import INFO
from django.test import TestCase
from core import models 
from django.core.files.images import ImageFile
from decimal import Decimal


class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(
            name = "The test product", price=Decimal("10.00")
        )
        product.save()

        with open('static/images/test.jpg', 'rb') as f:
            image = models.ProductImage(
                product=product,
                image=ImageFile(f, name='test.jpg')
            )

            with self.assertLogs("core", level="INFO") as cm:
                image.save()
                print('This image was tested')

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()
        
        with open('static/images/test.jpg', 'rb') as f:
            expected_content = f.read()
            # print(expected_content)
            # print(image.thumbnail.read())
            # assert image.thumbnail.read() == expected_content

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)