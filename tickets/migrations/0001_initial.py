# Generated by Django 4.2.5 on 2023-09-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('description', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('new', 'New'), ('done', 'Done')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
