# Generated by Django 4.2.5 on 2023-09-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.AddField(
            model_name='usertoken',
            name='username',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
