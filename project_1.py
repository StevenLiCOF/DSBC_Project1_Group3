# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:40:08 2015

@author: skh469
"""

import os
import json
from pprint import pprint

MOJO_DIR = os.path.join('data','boxofficemojo') 
META_DIR = os.path.join('data','metacritic') 
def get_movies(directory):
    '''Returns a list of dictionaries containing information in the
    JSON files of the provided directory, and prints the number
    of movies read'''
    file_contents = os.listdir(directory)
    movie_list=[]
    for filename in file_contents:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)
        if type(movie_data) == dict:
            movie_list.append(movie_data)
    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list
mojomovies=get_movies(MOJO_DIR)
metacriticmovies=get_movies(META_DIR)
from datetime import datetime

for movie in mojomovies:
    if movie['release_date_limited']:
        movie['release_date_limited']=datetime.strptime(movie['release_date_limited'],'%Y-%m-%d').date()
    if movie['release_date_wide']:
        movie['release_date_wide']=datetime.strptime(movie['release_date_wide'],'%Y-%m-%d').date()
import numpy as np
import pandas as pd

mojo_df = pd.DataFrame(mojomovies)
meta_df = pd.DataFrame(metacriticmovies)
meta_df['year']=meta_df['year'].replace('',np.nan)
meta_df=meta_df.sort('year')
meta_df=meta_df.dropna(subset=['title','year'],how='any')
mojo_df=mojo_df.dropna(subset=['title','year'],how='any')
meta_df['intyear']=[int(year) for year in meta_df['year']]
mojo_df['intyear']=[int(year) for year in mojo_df['year']]
meta_df['upper_title']= map(lambda x: x.upper(), meta_df['title'])
mojo_df['upper_title']= map(lambda x: x.upper(), mojo_df['title'])
merged_df = pd.merge(meta_df, mojo_df, how='outer', on='upper_title')
#print mojo_df.shape
#print meta_df.shape
#print merged_df.shape
#print mojo_df.columns.values
#print meta_df.columns.values
#print merged_df.columns.values
merged_df=merged_df.sort('upper_title')
#merged_years=merged_df[['year_x','year_y']]
#merged_directors=merged_df[['director_x','director_y']]
#both_directors=merged_directors.dropna(axis=0)
#notequal_directors=both_directors[both_directors.director_x!=both_directors.director_y]
#both_years=merged_years.dropna(axis=0)
#notequal_years=both_years[both_years.year_x!=both_years.year_x]
#meta_df['str_title']=[str(title) for title in meta_df[['title']]]
#meta_df['str_title']=map(lambda x: str(x), meta_df[['title']])
#[type(title) for title in meta_df[['title']]]
#[str(title) for title in meta_df[['title']]]

#print str(1000)
merged_df['year'] = merged_df['year_x'].fillna(merged_df['year_y'])
merged_df=merged_df.dropna(subset=['year'])
merged_df['year']=map(lambda x: int(float(x)), merged_df['year'])
float('2008.0')
merged_df['director'] = merged_df['director_x'].fillna(merged_df['director_y'])
merged_df=merged_df.dropna(subset=['year'])
merged_df['year'] = map(lambda x: int(x), merged_df['year'])
merged_df['title_len']=merged_df[len('title')]
modelinputs = merged_df[['title',
                         'year',
                         'genre',
                         'release_date',
                         'runtime_minutes',
                         'studio',
                         'production_budget',
                         'release_date_limited',
                         'director',
                         'worldwide_gross']].dropna(subset=['worldwide_gross'])
merged_df.columns.values
mojo_df.columns.values
meta_df.columns.values
mojo_budget=mojo_df.dropna(subset=['production_budget'])
print mojo_budget.shape