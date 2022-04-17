# Generated by Django 3.2.12 on 2022-04-16 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0013_alter_blogdetailpage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
    ]