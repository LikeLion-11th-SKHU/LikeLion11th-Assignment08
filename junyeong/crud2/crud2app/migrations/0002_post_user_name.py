# Generated by Django 4.2.1 on 2023-06-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
