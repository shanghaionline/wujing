from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
import re

class SignUpForm(forms.Form):
    username = forms.CharField(label='用户名', max_length = 20)
    password = forms.CharField(label='密码', widget = widgets.PasswordInput)
    password_again = forms.CharField(label='密码', widget = widgets.PasswordInput)

    def clean_username(self):
    	data = self.cleaned_data['username']
    	prog = re.compile(r'[a-zA-Z0-9_]+')
    	if not prog.match(data):
    		raise forms.ValidationError('用户名只能包含英文字符，数字及下划线', code='invalid_username')
    	if User.objects.filter(username = data):
    		raise forms.ValidationError("用户名已经存在", code='username_exists')
    	return data

    def clean_password_again(self):
        data = self.cleaned_data['password_again']
        if not data == self.cleaned_data['password']:
            raise forms.ValidationError('两次密码不相同', code='password_again_err')

class SignInForm(forms.Form):
    username = forms.CharField(label='用户名', max_length = 20)
    password = forms.CharField(label='密码', widget = widgets.PasswordInput)

class ChangePasswdForm(forms.Form):
    password_old = forms.CharField(label='旧密码')
    password = forms.CharField(label='新密码')
    password_again = forms.CharField(label='新密码')

    def clean_password_again(self):
        data = self.cleaned_data['password_again']
        if not data == self.cleaned_data['password']:
            raise forms.ValidationError('两次密码不相同', code='password_again_err')
