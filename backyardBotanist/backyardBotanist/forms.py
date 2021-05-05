from django import forms

class userLoginForm(forms.Form):
    email = forms.EmailField()

class groupForm(forms.Form):
    group = forms.CharField(label='Taxonomic Group')

class subGroupForm(forms.Form):
    subgroup = forms.CharField(label='Taxonomic Subgroup')
