from django import forms
from captcha.fields import CaptchaField
from .models import *

class Add_Question_Form(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Pregunta
		#exclude = ['user','facebook']

"""class Add_Question_Form(forms.Form):
	titulo = forms.CharField(required=True , widget=forms.TextInput())
"""
	