#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('train.csv')
label = dataset['class']
x = ['ID','age','sex','chest','resting_blood_pressure','serum_cholestoral','fasting_blood_sugar','resting_electrocardiographic_results','maximum_heart_rate_achieved','exercise_induced_angina','oldpeak','slope','number_of_major_vessels','thal']
features = dataset[x]

test = pd.read_csv('test.csv')
#test_y = test['class']
test_x = test[x]

print('Stage 1')

import csv
from sklearn import svm
from sklearn.model_selection import train_test_split

print('Stage 2')

x_train,x_test,y_train,y_test = train_test_split(features,label,test_size=0.5,random_state=2)
model = svm.SVC(kernel='linear',random_state=1)
print('Stage 3')
model.fit(x_train,y_train)
print('Stage 4')
print(model.score(x_test,y_test))

def output():
    csvData = [['ID','class']]
    for i in range(len(result)):
        csvData.append([test['ID'][i],result[i]])
    csvFile = open('final_ans.csv','w',newline='')
    writer = csv.writer(csvFile)
    for data in csvData:
        writer.writerow(data)
    csvFile.close()
