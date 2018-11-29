from django.forms import ModelForm,ValidationError
from .models import Tweet

class TweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        
        if content == '1234':
            raise ValidationError('not 1234')
        else:
            return content
