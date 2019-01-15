from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]
        #exclude = ['user']

    def clean_content(self, *args, **kwargs):
        content = 'abc'
        if content == 'abc':
            raise forms.ValidationError('Cannot be abc')
        return content