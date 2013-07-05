from django import  newforms as forms

class RegistrationForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  email = forms.EmailField(label='Email Address')
  password1 = forms.CharField(label='Password', max_length=60)
  password2 = forms.CharField(label='Confirm Password', max_length=60)