

# Data taken from https://www.kaggle.com/toramky/automobile-dataset
import numpy as np
import os
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
import time
# kmodes library: https://github.com/nicodv/kmodes
from kmodes.kprototypes import KPrototypes
'''
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")

df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/datav2.csv', sep=',',na_values='?')
df = df.dropna(subset = ['Price'])

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
        age_approx.append('0')
    else:
        age_approx.append(row['Age'][0]+'0')

demo = demo.assign(age_approx=pd.Series(age_approx).values)
demo = demo.drop(demo[demo.age_approx == 'A0'].index)

name_list = demo.columns.values
for name in name_list[5:]:
    demo[name] = pd.to_numeric(demo[name])

unique_age = list(demo['age_approx'].unique())
unique_gender = list(demo['Gender'].unique())
table = {}
for age in unique_age:
    for gender in unique_gender:
        table[(age, gender)] = {}
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

for age_gender, value in table.items():
    new_dict = value.copy()
    for model, tot in table[age_gender].items():
        if not model in list(df['Model']):
            new_dict.pop(model, None)
    table[age_gender] = new_dict

for age_gender, value in table.items():
    table[age_gender] = list(table[age_gender].items())

from operator import itemgetter
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
'''


def second_stage(df, age1, gender, brand, table):
    """
    Recommends a list of cars that satisfies the specified age and preferred brand.
    If brand is a nationality ('Korea', 'Japan', or 'Germany'), add weights to the
    corresponding car of the associated country. If brand is 'Luxury', add weights
    to each car according to its price.

    Inputs:
    - df: data frame, data to filter
    - age: string, age in approximation (e.g.,'30' for 30s)
    - gender: stirng, either 'M' or 'F'
    - brand: string, either 'Korea', 'Japan', 'Germany', or 'Luxury'

    Outputs:
    - filtered: dataframe, containing objects satisfying the conditions
    """
    filtered = None
    scores = []
    for index, row in df.iterrows():
        score = 0
        if row['Model'] in table[(int(age1),gender)]:
            score += table[(int(age1),gender)][row['Model']]
        if brand != 'Luxury':
            if row['Country'] == brand:
                score += 1
        else:
            score += row['luxury_weight']
        scores.append(score)
    df = df.assign(scores=pd.Series(scores).values)
    filtered = df.nlargest(int(1/2*len(df.index)), 'scores', 'first')
    return filtered



# kmodes library: https://github.com/nicodv/kmodes
def third_stage(df, wage, car_type, small_car, hybrid):
    """
    Recommends a list of cars based on specified car_type, small_car, budget1,
    budget2, using kmodes algorithm. If car_type is normal, small_car will be
    considered as a replacement. Overall, the net effect of car_type and small_car
    is one of the followings: 'MIDDLE', 'COMPACT', 'BIG', 'SUV/VR', 'SPORT', 'SMALL'

    Inputs:
    - df: data frame, to filter
    - wage: string, either '15', '15-30', '30-60', or '60'
    - car_type: string, either 'NORMAL', 'SUV/VR', or 'SPORT'
    - small_car: string, either 'SMALL/COMPACT', 'MIDDLE', or 'BIG'
    - hybrid: string, 'X' or 'O'
    """
    # According to Weiting's suggestion
    if wage == '15':
        budget = 1500/2
    elif wage == '15-30':
        budget = (4000+1500)/2
    elif wage == '30-60':
        budget = (4000+7000)/2
    elif wage == '60':
        budget = (16931+7000)/2

    X_train = df[['Price','Car type', 'EV/Hybrid available' ]].values
    kproto = KPrototypes(n_clusters=5, init='Huang', verbose=0)
    clusters = kproto.fit(X_train, categorical=[1,2]).labels_
    if car_type != 'NORMAL':
        net_car_type = car_type
    else:
        net_car_type = small_car
    X_test = np.array([[budget, net_car_type, hybrid]])
    X_df =  pd.DataFrame(X_test)
    X_df[[0]]=X_df[[0]].astype('float')
    X_test = X_df.values
    labels = kproto.predict(X_test, categorical=[1,2])
    fil_mask = df.assign(cluster=clusters)
    fil_mask = fil_mask[fil_mask.cluster==labels[0]].drop(axis=1, columns='cluster')

    num_rec = 3 # JUST NEED TO SPECIFY THE NUMBER OF RECOMMENDATIONS HERE

    return fil_mask.nlargest(num_rec, 'scores', 'first')
