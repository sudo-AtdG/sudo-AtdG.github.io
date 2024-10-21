from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=40, default='Untitled')
    anons = models.CharField('Anons', max_length=300)
    full_text = models.TextField('Text')
    date = models.DateTimeField(
        'Date',
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'