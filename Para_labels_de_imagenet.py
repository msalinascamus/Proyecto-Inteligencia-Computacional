# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:44:05 2019

@author: migue
"""

#Para extraer labels del archivo de imagenet

#%%

clases = list()
histogram = dict() #clase->ocurrencias de esa clase 
count = 0
last_imageid='null'
with open('fall11_urls.txt','r',encoding='utf-8',errors='ignore') as imagenet:
    splitted_line = imagenet.readline().split('\t')
    imageid = splitted_line[0].split('_')[0][0:5:1]
    clases.append(imageid)
    for line in imagenet:
        splitted_line = line.split('\t')
        imageid = splitted_line[0].split('_')[0][0:5:1]
        count += 1
        if imageid != clases[-1]:
            clases.append(imageid)
            histogram[last_imageid] = count
            count = 0
        last_imageid = imageid
    histogram[imageid] = count

#%%
new_histogram = {}
for key, value in histogram.items():
    if value > 35000:
        new_histogram[key] = value

print(len(new_histogram))

#%%
import matplotlib.pyplot as plt
plt.figure(figsize=(40,20))
plt.bar(new_histogram.keys(), new_histogram.values(),color='g')
plt.xticks(size='xx-large',rotation=45)
plt.yticks(size='xx-large',rotation=45)
plt.savefig('histogram.pdf',bbox_inches='tight')


