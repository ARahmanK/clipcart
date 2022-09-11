# Generated by Django 4.0.6 on 2022-09-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]