import numpy as np
import pandas as pd
# kmodes library: https://github.com/nicodv/kmodes
from apps.kmodes.kmodes.kprototypes import KPrototypes
# Data taken from https://www.kaggle.com/toramky/automobile-dataset

def first_stage(df, price, drive_wheels):
    """
    Recommends a list of cars that satisfies the specified price and drive_wheels

    Inputs:
    - df: the data frame to filter
    - price: tuple of two floats-- the lower bound and upper bound
    - drive_wheels: a list of strings of the preferred type of drive_wheels

    Outputs:
    - filtered: a dataframe containing objects satisfying the conditions
    """
    mask_drive_wheels = df.drive_wheels
    filtered = df[(price[0] <= df.price) &(df.price <= price[1]) & (df.drive_wheels.isin(drive_wheels))]
    return filtered


def second_stage(df, num_of_doors, aspiration):
    """
    Recommends a list of cars that satisfies the specified highway_mpg, horsepower, body_style

    Inputs:
    - df: the data frame to filter
    - num_of_doors: tuple of two floats-- the lower bound and upper bound
    - aspiration: a list of strings of the preferred type of aspiration

    Outputs:
    - filtered: a dataframe containing objects satisfying the conditions
    """

    weights = [10,100]
    ranks = []
    doors_dict = {'two': 2,
                 'four': 4}
    for index, row in df.iterrows():
        doors_score = num_of_doors[0] <= doors_dict[row['num_of_doors']] <= num_of_doors[1]
        aspiration_score = row['aspiration'] in aspiration
        rank = weights[0]*doors_score + weights[1]*aspiration_score
        ranks.append(rank)
    df = df.assign(ranks=pd.Series(ranks).values)
    filtered = df.nlargest(int(1/2*len(df.index)), 'ranks', 'first').drop(axis=1, columns='ranks')
    return filtered

# kmodes library: https://github.com/nicodv/kmodes

def third_stage(df, highway_mpg, city_mpg, body_style, horsepower):
    """
    Recommends a list of cars that satisfies the specified highway_mpg, horsepower, body_style.
    Using k-prototype algorithm.

    Inputs:
    - df: the data frame to filter
    - highway_mpg, city_mpg, horsepower: tuples of two floats-- the lower bound and upper bound
    - body_style: string, the preferred type of body_style
    """
    X_train = df[['highway_mpg', 'city_mpg', 'body_style', 'horsepower']].values
    kproto = KPrototypes(n_clusters=4, init='Huang', verbose=0)
    clusters = kproto.fit(X_train, categorical=[2]).labels_
    X_test = np.array([[np.mean(highway_mpg),np.mean(city_mpg), body_style, np.mean(horsepower)]])
    X_df =  pd.DataFrame(X_test)
    X_df[[0,1,3]]=X_df[[0,1,3]].astype('float')
    X_test = X_df.values
    labels = kproto.predict(X_test, categorical=[2])
    fil_mask = df.assign(cluster=clusters)
    return fil_mask[fil_mask.cluster==labels[0]].drop(axis=1, columns='cluster')
