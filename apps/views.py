from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
import os
import pandas as pd
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import NameForm
import apps.algo

df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/Automobile_data.csv', sep=',',na_values='?')
df.head(10)

old_names = df.columns.values
new_names = [name.replace('-','_') for name in old_names]
df.rename(columns = dict(zip(old_names, new_names)), inplace = True)
df.columns.values

df = df.dropna(subset = ['price', 'drive_wheels','highway_mpg', 'city_mpg','body_style','horsepower',
                           'num_of_doors','aspiration'])

def index(request):
    return HttpResponse("Hello, world.")

def form(request):
    return render_to_response('apps/form.html')

def get_name(request):
    form = NameForm()
    return render(request, 'name.html', {'form': form})

def get_data(request):
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        if form.is_valid():
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            data = form.cleaned_data
            price = tuple([float(num.strip()) for num in data['price'].split(',')])
            drive_wheels = data['drive_wheels'].split(',')
            fil1 = apps.algo.first_stage(df, price, drive_wheels)
            num_of_doors = tuple([float(num.strip()) for num in data['num_of_doors'].split(',')])
            aspiration = data['aspiration'].split(',')
            fil2 = apps.algo.second_stage(fil1, num_of_doors, aspiration)
            highway_mpg = tuple([float(num.strip()) for num in data['highway_mpg'].split(',')])
            city_mpg = tuple([float(num.strip()) for num in data['city_mpg'].split(',')])
            horsepower = tuple([float(num.strip()) for num in data['horsepower'].split(',')])
            body_style = data['body_style']
            fil3 = apps.algo.third_stage(fil2, highway_mpg, city_mpg, body_style, horsepower)

    else:
        form = NameForm()
    return HttpResponse(fil3.to_html())
