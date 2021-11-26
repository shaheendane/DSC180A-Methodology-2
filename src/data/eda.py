#dont have our actual dataset yet, we have to complete a training in order to access data
#using first dataset we worked with to do some basic EDA
#print('hello-world')

import pandas as pd
import numpy as np

def basic_eda(data):
    femtemp = pd.read_excel(data, 'FemTemp')
    femact = pd.read_excel(data, 'FemAct')
    maletemp = pd.read_excel(data, 'MaleTemp')
    maleact = pd.read_excel(data, 'MaleAct')

    clean = femtemp.iloc[:17280,]
    df = pd.DataFrame()
    # combine the 3 cycles
    for i in range(0,17280, 5760):
        df = pd.concat([df,clean.iloc[i:i+5760,].reset_index().drop(['index'],axis =1)],axis = 1,ignore_index=True)
    df.drop([0], axis=1).mean(axis = 1)
    df.drop([0], axis=1).mean(axis = 1).plot(title = 'Female')

    df['avg'] = df.drop([0], axis=1).mean(axis = 1)
    df.boxplot(column = ['avg'])



    clean = maletemp.iloc[:17280,]
    df = pd.DataFrame()
    # combine the 3 cycles
    for i in range(0,17280, 5760):
        df = pd.concat([df,clean.iloc[i:i+5760,].reset_index().drop(['index'],axis =1)],axis = 1,ignore_index=True)
    
    df.drop([0], axis=1).mean(axis = 1)
    df.drop([0], axis=1).mean(axis = 1).plot(title = 'Male')



    clean = femact.iloc[:17280,]
    df = pd.DataFrame()
    # combine the 3 cycles
    for i in range(0,17280, 5760):
        df = pd.concat([df,clean.iloc[i:i+5760,].reset_index().drop(['index'],axis =1)],axis = 1,ignore_index=True)
    df.drop([0], axis=1).mean(axis = 1)
    df.drop([0], axis=1).mean(axis = 1).plot(title = 'Female ACT')



    clean = maleact.iloc[:17280,]
    df = pd.DataFrame()
    # combine the 3 cycles
    for i in range(0,17280, 5760):
        df = pd.concat([df,clean.iloc[i:i+5760,].reset_index().drop(['index'],axis =1)],axis = 1,ignore_index=True)
    df.drop([0], axis=1).mean(axis = 1)
    df.drop([0], axis=1).mean(axis = 1).plot(title = 'Male ACT')

    df['avg'] = df.drop([0], axis=1).mean(axis = 1)
    df.boxplot(column = ['avg'])
