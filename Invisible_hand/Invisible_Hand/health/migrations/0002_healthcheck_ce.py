# Generated by Django 3.1.6 on 2021-03-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcheck',
            name='CE',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
