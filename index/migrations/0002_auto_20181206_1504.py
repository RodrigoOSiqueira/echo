# Generated by Django 2.1.3 on 2018-12-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='link',
            field=models.CharField(default=' ', max_length=150, verbose_name='Link Site'),
        ),
        migrations.AddField(
            model_name='projet',
            name='tipo',
            field=models.CharField(default=' ', max_length=50, verbose_name='Tipo Projeto'),
        ),
    ]
