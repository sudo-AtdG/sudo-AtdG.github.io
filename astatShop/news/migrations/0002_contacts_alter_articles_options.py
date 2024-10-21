# Generated by Django 5.1.1 on 2024-09-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'News'},
        ),
    ]
