# Generated by Django 4.0.5 on 2022-06-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lacrei', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='descricao',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='todo',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
