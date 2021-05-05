from django import forms

class userLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)

class userChangePasswordForm(forms.Form):
    email = forms.EmailField()
    oldPassword = forms.CharField(max_length=30)
    newPassword = forms.CharField(max_length=30)

class userCreateAccountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    confirmPassword = forms.CharField(max_length=30)
