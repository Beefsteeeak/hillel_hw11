import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReminderForm(forms.Form):
    email = forms.EmailField(required=True, help_text='Enter email to send message')
    text = forms.CharField(required=True, widget=forms.Textarea, help_text='Enter text to remind')
    datetime = forms.DateTimeField(required=True, help_text='Enter datetime when to get the reminder')

    def clean_datetime(self):
        data = self.cleaned_data['datetime']

        if data < timezone.now() + datetime.timedelta(hours=3):
            raise ValidationError('Invalid date - datetime cannot be in the past')

        if data > timezone.now() + datetime.timedelta(days=2, hours=3):
            raise ValidationError('Invalid date - datetime cannot be more than 2 days ahead')

        return data
