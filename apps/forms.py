from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    price_lower = forms.FloatField(label='price lower')
    price_upper = forms.FloatField(label='price upper', min_value=price_lower)
    drive_wheels = forms.CharField(label='drive wheels')




    # data = self.cleaned_data
    # return data
