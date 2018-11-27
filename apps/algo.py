

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
    print("hello", table[(int(age1),gender)])
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
    print("DATAFIELD: ", df)
    filtered = df.nlargest(int(1/2*len(df.index)), 'scores', 'first')
    print("FILTERED: ", filtered)
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
    if wage == '0-15':
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
    print("FINAL: ", fil_mask)
    return fil_mask.nlargest(num_rec, 'scores', 'first')
