# Generated by Django 2.1.1 on 2018-09-08 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_date']},
        ),
    ]
