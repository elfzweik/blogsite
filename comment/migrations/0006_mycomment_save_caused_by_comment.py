# Generated by Django 4.0.4 on 2022-09-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_alter_mycomment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycomment',
            name='save_caused_by_comment',
            field=models.BooleanField(default=False),
        ),
    ]