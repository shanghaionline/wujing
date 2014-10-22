from django import forms
from django.forms import widgets

class PushMessageForm(forms.Form):
	target = forms.IntegerField()
	message = forms.CharField()

	
