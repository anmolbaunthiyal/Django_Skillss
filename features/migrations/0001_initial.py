# Generated by Django 3.2.4 on 2021-06-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact', models.IntegerField(max_length=15)),
                ('interest', models.CharField(max_length=255)),
            ],
        ),
    ]
