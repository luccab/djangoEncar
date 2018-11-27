
# django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from operator import itemgetter

# app
from .forms import NameForm
from .models import Person
import apps.algo

import numpy as np
import os
import scipy as sp
# import matplotlib as mpl
# import matplotlib.cm as cm
# import matplotlib.pyplot as plt
import pandas as pd
# import time
import seaborn as sns
# kmodes library: https://github.com/nicodv/kmodes
# from kmodes.totypes import KPrototypes

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)

sns.set_style("whitegrid")
sns.set_context("poster")


df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/EncarDatasetEncoded.csv', sep=',',na_values='?')
df = df.dropna(subset = ['Price']) # remove rows without data in Price column

df['PRICE_RANK'] = df['Price'].rank(ascending=True)
luxury_weights = []
for index, row in df.iterrows():
    if row['PRICE_RANK'] < len(df.index)/3:
        luxury_weights.append(0)
    elif row['PRICE_RANK'] < 2*len(df.index)/3:
        luxury_weights.append(1)
    else:
        luxury_weights.append(2)
df = df.assign(luxury_weight=pd.Series(luxury_weights).values)




demo = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/demo_data.csv', sep=',',na_values='?')
age_approx = []
for index, row in demo.iterrows():
    if row['Age'][0]=='~':
        age_approx.append('0') # ~10
    else:
        age_approx.append(row['Age'][0]+'0')

demo = demo.assign(age_approx=pd.Series(age_approx).values)
demo = demo.drop(demo[demo.age_approx == 'A0'].index)


name_list = demo.columns.values
print(name_list)
for name in name_list[5:]:
    demo[name] = pd.to_numeric(demo[name])

unique_age = list(demo['age_approx'].unique())
unique_gender = list(demo['Gender'].unique())
table = {}
for age in unique_age:
    for gender in unique_gender:
        table[(age, gender)] = {}
print(table)
for index, row in demo.iterrows():
    num_list = []
    for name in name_list[5:-1]:
        num_list.append(row[name])
    if row['Model'] in table[(row['age_approx'], row['Gender'])]:
        table[(row['age_approx'], row['Gender'])][row['Model']] += num_list
    else:
        table[(row['age_approx'], row['Gender'])][row['Model']] = num_list
for age_gender, value in table.items():
    for model, num_list in value.items():
        table[age_gender][model] = np.mean(table[age_gender][model])
    # print(age_gender, "=========")
    # print(table[age_gender])

for age_gender, value in table.items():
    new_dict = value.copy()
    for model, tot in table[age_gender].items():
        if not model in list(df['Model']):
            new_dict.pop(model, None)
    table[age_gender] = new_dict

for age_gender, value in table.items():
    table[age_gender] = list(table[age_gender].items())


for age_gender, value in table.items():
    sorted_scores = sorted(value, key=itemgetter(1))
    new_dict = {}
    for i in range(len(sorted_scores)):
        if i <= len(sorted_scores)//3:
            new_dict[sorted_scores[i][0]] = 0
        elif i <= 2*len(sorted_scores)//3:
            new_dict[sorted_scores[i][0]] = 1
        else:
            new_dict[sorted_scores[i][0]] = 2
    table[age_gender] = new_dict
    print(age_gender, "=========")
    print(new_dict)




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
            '''
            drive_wheels = data['drive_wheels'].split(',')
            fil1 = apps.algo.first_stage(df, price, drive_wheels)
            num_of_doors = tuple([float(num.strip()) for num in data['num_of_doors'].split(',')])
            aspiration = data['aspiration'].split(',')
            '''
            print("DATA:", data)
            fil2 = apps.algo.second_stage(df, data['age'], data['gender'], data['brand'], table)

            fil3 = apps.algo.third_stage(fil2, data['wage'], data['car_type'], data['small_car'], data['hybrid'])

    else:
        form = NameForm()
    return HttpResponse(fil3.to_html())
