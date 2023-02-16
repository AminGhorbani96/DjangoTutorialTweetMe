from django import forms
from django.core.exceptions import ValidationError

from Tweet import models

MAX_TWEET_LEN = 5
class TweetForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ["details"]

    def clean_details(self):
        content = self.cleaned_data.get("details")
        if len(content) > MAX_TWEET_LEN:
            raise ValidationError("too long message")
        return content