from django import forms

class BoardMsgForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)
    tag = forms.CharField()
