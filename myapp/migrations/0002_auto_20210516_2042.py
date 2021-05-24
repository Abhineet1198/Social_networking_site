# Generated by Django 3.1.5 on 2021-05-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='HomeTown',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='currentTown',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='friend',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='img',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='qualification',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='relationship',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='accountuser',
            name='work',
            field=models.CharField(default=None, max_length=500),
        ),
    ]