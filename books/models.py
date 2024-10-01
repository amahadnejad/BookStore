from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('User'), on_delete=models.CASCADE)  # Connect To User
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    author = models.CharField(verbose_name=_('Author'), max_length=200)
    translator = models.CharField(verbose_name=_('Translator'), max_length=200, blank=True)
    publisher = models.CharField(verbose_name=_('Publisher'), max_length=200)
    description = models.TextField(verbose_name=_('Description'))
    price = models.PositiveIntegerField(verbose_name=_('Price'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('Cover'),)
    is_active = models.BooleanField(default=True, verbose_name=_('Is_Active'),)

    # Automatic DateFields
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime_Created'),)
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Datetime_Modified'),)

    def __str__(self):
        return f"{self.author}: {self.title}"

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Connect To User Model
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')  # Connect To Book Model
    text = models.TextField(verbose_name=_('Text'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is-Active'))
    recommend = models.BooleanField(default=True, verbose_name=_('Recommend'))

    # Automatic DateField
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime_Created'),)

    def __str__(self):
        return self.text
