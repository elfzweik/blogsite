# Generated by Django 3.2.12 on 2022-05-04 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_blogdetailpage_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='collection',
        ),
    ]
