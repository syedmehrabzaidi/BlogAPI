# Generated by Django 2.2.6 on 2021-11-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecustomuser',
            name='user',
            field=models.TextField(),
        ),
    ]
