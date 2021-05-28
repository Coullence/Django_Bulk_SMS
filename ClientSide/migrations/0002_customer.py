# Generated by Django 2.2.10 on 2021-03-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('homeCounty', models.CharField(max_length=100)),
                ('homeTown', models.CharField(max_length=100)),
                ('currentCounty', models.CharField(max_length=100)),
                ('currentTown', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
