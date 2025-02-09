# Generated by Django 4.2.8 on 2024-02-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('comment', models.TextField(max_length=999)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]
