# Generated by Django 4.2.1 on 2023-05-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
