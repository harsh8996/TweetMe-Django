from django.contrib import admin
from .forms import TweetModelForm
# Register your models here.

from .models import Tweet

admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    class meta:
        model = Tweet
        form = TweetModelForm
    
admin.site.register(Tweet,TweetModelAdmin)