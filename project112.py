import pandas as pd
import plotly.express as p
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import numpy as np

'''reading the data using pandas and csv'''
data_p = pd.read_csv('savings_data_final.csv')
quant_p = data_p['quant_saved'].to_list()
data_age = data_p['age'].to_list()

with open('savings_data_final.csv','r') as f:
    frame = csv.reader(f)
    data_c = list(frame)

'''ploting the graph'''
scatter = p.scatter(data_p,y='quant_saved',color='rem_any',title='The Reminder Graph')
#scatter.show()

'''printing the mean median mode and stdev of the data[quantity]'''
print(f'the mean of data is -- {statistics.mean(quant_p)}')
print(f'the median of data is -- {statistics.median(quant_p)}')
print(f'the mode of data is -- {statistics.mode(quant_p)}')
print(f'the stdev of data is -- {statistics.stdev(quant_p)}')

'''finding mean median mode of 2 different sampling of data [50,100] 1000 times'''
def randomcount(count):
    data_list = []
    for i in range(count):
        value = random.randint(0,len(quant_p))
        data_list.append(quant_p[value])
    mean = statistics.mean(data_list)
    return data_list 

temp_list1 = randomcount(50)
temp_list2 = randomcount(100)
print('{} is the mean of 50 random sample'.format(float(statistics.mean(temp_list1))))
print(f'{statistics.mean(temp_list2)} is the mean of 100 random sample')

print(f'{statistics.stdev(temp_list1)} is the stdev of the sample 1')
print(f'{statistics.stdev(temp_list2)} is the stdev of the sample 2')

age = []
savings = []
for a in quant_p:
    for i in data_age:
        if float(i) != 0:
            age.append(float(i))
            savings.append(float(a))

correlation = np.corrcoef(age,savings)
print(f'correlation -- {correlation[0,1]}')