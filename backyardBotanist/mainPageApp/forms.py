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

class deleteAccountForm(forms.Form):
    userID = forms.IntegerField()

class searchPlantForm(forms.Form):
    plant = forms.CharField(max_length=100)

class addSightingForm(forms.Form):
    sightingid = forms.CharField(max_length=30)
    userid = forms.CharField(max_length=30)
    plantid = forms.CharField(max_length=30)
    county = forms.CharField(max_length=30)
    state = forms.CharField(max_length=30)

