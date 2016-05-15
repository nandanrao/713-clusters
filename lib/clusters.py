# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:54:17 2016

@author: Mpizos
"""

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import numpy as np


def get_all_genres(d):
   data = []
   for i in range(len(d)):
       data.extend(d[i]['genres'])
   return list(set(data))

def get_data(data):
    data = []
    unique_values = get_all_genres(data)
    for i in range(len(data)):
        temp = []
        temp.append(json_file[i]['id'])
        temp.append(json_file[i]['acousticness'])
        temp.append(json_file[i]['danceability'])
        temp.append(json_file[i]['energy'])
        temp.append(json_file[i]['instrumentalness'])
        temp.append(json_file[i]['liveness'])
        temp.append(json_file[i]['loudness'])
        temp.append(json_file[i]['popularity'])
        temp.append(json_file[i]['speechiness'])
        temp.append(json_file[i]['tempo'])
        temp.append(json_file[i]['valence'])
        temp_genres = json_file[i]['genres']
        dummy_genres = [int(x in temp_genres) for x in unique_values]
        temp.extend(dummy_genres)
        data.append(temp)
    return data

def split_id_features_to_np(data):
    ids = [x[0] for x in data]
    features = [x[1:] for x in data]
    return ids,np.array(features)

def get_song_and_artist(json):
    data = []
    for i in range(len(json)):
        temp = []
        temp.append(json[i]['artists'][0]['name'])
        temp.append(json[i]['name'])
        data.append(temp)
    return data

def get_song_genre(json_file,indexes):
    data = []
    for i in indexes:
        data.extend(d[i]['genres'])
    return data


def get_artist_id(json_file,indexes):
    data = []
    for i in indexes:
        data.extend([json_file[i]['artists'][0]['id']])
    return data

def do_it (d):
    data = get_data(d)
    ids,features = split_id_features_to_np(data)
    af = AffinityPropagation(preference=-200).fit(features)
    counts = np.bincount(af.labels_)
    highest_cluster = np.argmax(counts)
    index_of_choused_cluster = np.where(af.labels_==highest_cluster)[0]
    features_of_chosen_songs = [features[i][:10] for i in index_of_choused_cluster]
    relevant_genres = get_song_genre(d,index_of_choused_cluster)
    mean_values = np.mean(features_of_chosen_songs,axis=0)

    Dictionary_song_features = {'features':{}}
    Dictionary_song_features['features']['acousticness'] = mean_values[0]
    Dictionary_song_features['features']['danceability']= mean_values[1]
    Dictionary_song_features['features']['energy'] = mean_values[2]
    Dictionary_song_features['features']['instrumentalness'] = mean_values[3]
    Dictionary_song_features['features']['liveness'] = mean_values[4]
    Dictionary_song_features['features']['loudness'] = mean_values[5]
    Dictionary_song_features['features']['popularity'] = mean_values[6]
    Dictionary_song_features['features']['speechiness'] = mean_values[7]
    Dictionary_song_features['features']['tempo'] = mean_values[8]
    Dictionary_song_features['features']['valence'] = mean_values[9]
    Dictionary_song_features['artists'] = get_artist_id(d,index_of_choused_cluster)
    return Dictionary_song_features

# """
# pref = [0.1,0.5,1,10,20,50,100,200,1000,2000]
# for i in pref:
#     for j in [10,20,30,40]:
#         af = AffinityPropagation(preference=-i,affinity='precombuted').fit(features[:j])
#         labels = af.labels_
#         print("data size: "+str(j))
#         print("---pref: "+str(i))
#         cluster_centers_indices = af.cluster_centers_indices_
#         n_clusters_ = len(cluster_centers_indices)
#         print("------number of clusters:"+str(n_clusters_))

# """
