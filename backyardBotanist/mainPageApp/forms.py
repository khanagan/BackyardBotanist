from django import forms

class userLoginForm(forms.Form):
    email = forms.EmailField()


