# Generated by Django 4.0.1 on 2022-04-09 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teach',
        ),
        migrations.DeleteModel(
            name='faculty_alloc',
        ),
    ]
