from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_record', '0003_alter_userip_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP地址'),
        ),
    ]
