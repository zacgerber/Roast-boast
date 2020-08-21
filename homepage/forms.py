from django import forms
from homepage.models import TalkingsOn


class ConvoForm(forms.ModelForm):
    class Meta:
        model = TalkingsOn
        fields = ['choices', 'body']

