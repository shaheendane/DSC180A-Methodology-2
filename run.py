#dont have our actual dataset yet, we have to complete a training in order to access data
#using first dataset we worked with to do some basic EDA
#print('hello-world')

import pandas as pd
import numpy as np

xls = pd.ExcelFile('test/testdata/Smarr PeerJ Data.xlsx')
femtemp = pd.read_excel(xls, 'FemTemp')
femact = pd.read_excel(xls, 'FemAct')
maletemp = pd.read_excel(xls, 'MaleTemp')
maleact = pd.read_excel(xls, 'MaleAct')

print(femtemp.describe())
print(femact.describe())
print(maletemp.describe())
print(maleact.describe())
