# Generated by Django 4.2.4 on 2023-09-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
                ('mark4', models.IntegerField()),
                ('mark5', models.IntegerField()),
            ],
        ),
    ]
