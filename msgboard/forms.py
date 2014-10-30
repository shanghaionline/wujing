from django import forms

class BoardMsgForm(forms.Form):
    content = forms.CharField(widget = forms.Textarea)
