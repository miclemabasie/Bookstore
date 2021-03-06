# Generated by Django 2.2 on 2021-11-29 03:27

from django.db import migrations

def capitalize(apps, schema_editor):
    Product = apps.get_model('core', "Product")
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_productimage_thumbnail'),
    ]

    operations = [
        migrations.RunPython(
            capitalize,
            migrations.RunPython.noop
        )
    ]
