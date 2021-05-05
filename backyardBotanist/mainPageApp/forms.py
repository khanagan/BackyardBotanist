from django import forms

class userLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


