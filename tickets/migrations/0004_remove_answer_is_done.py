# Generated by Django 4.2.5 on 2023-09-22 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_done',
        ),
    ]
