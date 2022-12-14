# Generated by Django 4.1.3 on 2022-11-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('bday', models.DateField(verbose_name='birthday')),
                ('tax_number', models.CharField(max_length=120, verbose_name='tax number')),
            ],
        ),
    ]
