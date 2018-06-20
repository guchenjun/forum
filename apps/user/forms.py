from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def check_data(self, username, password):
        if len(username) < 6:
            return "用户名不得小于6位"
        elif len(username) > 50:
            return "用户名不得大于50位"

        filter_result = User.objects.filter(username__exact=username)
        if len(filter_result) > 0:
            return "用户名已存在"

        if len(password) < 6:
            return "密码不得小于6位"
        elif len(password) > 20:
            return "密码不得大于20位"

        return "suc"


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError("This username does not exist.")
        return username
