from django import forms
from .models import Tweet

# class TweetModelForm(forms.ModelForm):
#     class meta:
#         model = Tweet
#         fields = ['user','content']

#     def clean_content(self):
#         content = self.cleaned_data['content']
        
#         if content == 'abc':
#             raise forms.ValidationError('not abc')
#         else:
#             raise forms.ValidationError('abc')

