# Generated by Django 4.1.6 on 2023-02-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='uuid',
            field=models.CharField(max_length=8, unique=True, verbose_name='uuid'),
        ),
    ]
