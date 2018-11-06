from django import forms

class NameForm(forms.Form):
    price = forms.CharField(label='Your budget:', help_text='Enter two numbers, \
    separated by comma')
    drive_wheels = forms.CharField(label='Drive wheels', help_text='Enter rwd, fwd, 4wd')
    num_of_doors = forms.CharField(label='No. Doors', help_text='Enter two numbers, \
    separated by comma')
    aspiration = forms.CharField(label='aspiration, separated by comma')
    highway_mpg = forms.CharField(label='Highway mpg',help_text='Enter two numbers, \
    separated by comma' )
    city_mpg = forms.CharField(label='city_mpg',help_text='Enter two numbers, \
    separated by comma')
    horsepower = forms.CharField(label='horsepower',help_text='Enter two numbers, \
    separated by comma')
    body_style = forms.CharField(label='body style')










    # data = self.cleaned_data
    # return data
