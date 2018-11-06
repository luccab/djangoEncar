from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    price_lower = forms.FloatField(label='price lower')
    price_upper = forms.FloatField(label='price upper')
    drive_wheels = forms.CharField(label='drive wheels')
    num_of_doors_lower = forms.FloatField(label='num of doors lower')
    num_of_doors_upper = forms.FloatField(label='num of doors upper')
    aspiration = forms.CharField(label='aspiration, separated by comma')
    highway_mpg_lower = forms.FloatField(label='highway_mpg_lower')
    highway_mpg_upper = forms.FloatField(label='highway_mpg_upper')
    city_mpg_lower = forms.FloatField(label='city_mpg_lower')
    city_mpg_upper = forms.FloatField(label='city_mpg_upper')
    horsepower_lower = forms.FloatField(label='horsepower_lower')
    horsepower_upper = forms.FloatField(label='horsepower_upper')
    body_style = forms.CharField(label='body style')
    









    # data = self.cleaned_data
    # return data
