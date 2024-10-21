from django.db import models


class Contacts(models.Model):
    name = models.CharField('Name', max_length=20)
    phone = models.CharField('Phone', max_length=100)
    email = models.EmailField('Email')
    date = models.DateTimeField(
        'Date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'