from django import forms

class InputForm(forms.Form):
	sentence = forms.CharField(max_length = 2000)

	def clean(self):
		cleaned_data = super(InputForm, self).clean()
		sentence = cleaned_data.get('sentence')
		if not sentence:
			raise forms.ValidationError("You have to enter a sentence!!")