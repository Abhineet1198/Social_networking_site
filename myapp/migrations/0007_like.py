# Generated by Django 3.1.5 on 2021-06-01 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210601_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('counter', models.IntegerField(default=0)),
                ('post', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
                ('user', models.ManyToManyField(blank=True, default=None, to='myapp.AccountUser')),
            ],
        ),
    ]
