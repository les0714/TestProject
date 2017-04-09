from django import forms
from appointment import models
from django.utils import formats


class UserData(forms.Form):
    user_date = forms.ModelChoiceField(queryset=models.MeetingDate.objects.all(),
                                  widget=forms.RadioSelect, initial=0)
    user_time = forms.ModelChoiceField(queryset=models.MeetingTime.objects.all(),
                                   widget=forms.RadioSelect, initial=0)
    user_name = forms.CharField(max_length=256,widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'required': ''}))
    user_email = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'required': ''}))

    def process(self, request) -> object:
        if self.is_valid():
            NewMeetingData = models.MeetingData(
                date=self.cleaned_data['user_date'],
                time=self.cleaned_data['user_time'],
                user_name=self.cleaned_data['user_name'],
                user_email=self.cleaned_data['user_email']
            )
            NewMeetingData.save()
            return self, True
        else:
            return self, False

