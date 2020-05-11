# Generated by Django 2.2.6 on 2020-05-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PandeminoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]