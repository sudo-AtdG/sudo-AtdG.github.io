# Generated by Django 5.1.1 on 2024-09-21 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_contacts_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]