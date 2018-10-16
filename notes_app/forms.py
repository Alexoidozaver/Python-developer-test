from django import forms

class note_form(forms.Form):
	name = forms.CharField(label='имя записи', max_length=100)
	text = forms.CharField(label='текст записи')