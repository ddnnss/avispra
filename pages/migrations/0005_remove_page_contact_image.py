# Generated by Django 2.2.3 on 2019-07-14 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190714_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='contact_image',
        ),
    ]
