from django import forms

class NameForm(forms.Form):
    # price_lower = forms.FloatField(label='price lower')
    # price_upper = forms.FloatField(label='price upper')
    price = forms.CharField(label='Your budget:', help_text='Enter two numbers, \
    separated by comma')
    drive_wheels = forms.CharField(label='Drive wheels', help_text='Enter rwd, fwd, 4wd')
    # num_of_doors_lower = forms.FloatField(label='num of doors lower')
    # num_of_doors_upper = forms.FloatField(label='num of doors upper')
    num_of_doors = forms.CharField(label='No. Doors', help_text='Enter two numbers, \
    separated by comma')
    aspiration = forms.CharField(label='aspiration, separated by comma')
    # highway_mpg_lower = forms.FloatField(label='highway_mpg_lower')
    # highway_mpg_upper = forms.FloatField(label='highway_mpg_upper')
    highway_mpg = forms.CharField(label='Highway mpg',help_text='Enter two numbers, \
    separated by comma' )
    # city_mpg_lower = forms.FloatField(label='city_mpg_lower')
    # city_mpg_upper = forms.FloatField(label='city_mpg_upper')
    city_mpg = forms.CharField(label='city_mpg',help_text='Enter two numbers, \
    separated by comma')
    # horsepower_lower = forms.FloatField(label='horsepower_lower')
    # horsepower_upper = forms.FloatField(label='horsepower_upper')
    horsepower = forms.CharField(label='horsepower',help_text='Enter two numbers, \
    separated by comma')
    body_style = forms.CharField(label='body style')










    # data = self.cleaned_data
    # return data
