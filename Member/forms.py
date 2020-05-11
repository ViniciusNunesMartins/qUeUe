from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    session = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Member
        fields = ['queue', 'priority', 'session']

        