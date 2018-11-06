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
#class FormView(generic.DetailView):
#    template_name = 'app/form.html'
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
        data = form.cleaned_data
        price = (data['price_lower'],data['price_upper'])
        drive_wheels = data['drive_wheels'].split(' ')
        fil1 = apps.algo.first_stage(df, price, drive_wheels)

        # redirect to a new URL:
        # return HttpResponseRedirect('/thanks/')
        return HttpResponseRedirect('/get_name/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
