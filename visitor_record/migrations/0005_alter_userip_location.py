from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_record', '0004_alter_userip_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='location',
            field=models.CharField(max_length=100, verbose_name='地理位置'),
        ),
    ]
