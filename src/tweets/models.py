from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import validate_content
from  django.urls import reverse
# Create your models here.

# def  check_content(value):
#     if value == '1234':
#         raise ValidationError('error...')
#     return value

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=150,validators=[validate_content])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def clean(self):
        content = self.content
        if content == '12345':
            raise ValidationError('not 12345')
        return super(Tweet,self).clean()

    def get_absolute_url(self):
        return reverse('tweet:detail',kwargs={'pk':self.pk})