import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gui as dfgui
# REQUIRED TO BE INSTALLED FOR gui MODULE: wxPython

greenPerformanceData=pd.read_excel('WP_CT_DA.xlsx')
# print(greenPerformanceData[greenPerformanceData['Total CBV'].isnull()==True])
# print(greenPerformanceData[greenPerformanceData['# of Orders'].isnull()==True])
null=greenPerformanceData.iloc[10]['Total CBV']
greenPerformanceData.replace(null,0,inplace=True)
service=greenPerformanceData['Service'].unique()
status=greenPerformanceData['Status of Order'].unique()
# print(service)
# print(status)

print(greenPerformanceData.head())
print(greenPerformanceData.tail())

print(greenPerformanceData)

dataMon1=greenPerformanceData[greenPerformanceData['Date'].apply(lambda x:x.month)==1]
dataMon2=greenPerformanceData[greenPerformanceData['Date'].apply(lambda x:x.month)==2]
dataMon3=greenPerformanceData[greenPerformanceData['Date'].apply(lambda x:x.month)==3]
dataMon4=greenPerformanceData[greenPerformanceData['Date'].apply(lambda x:x.month)==4]
# dataMon2=greenPerformanceData.loc['2016-01-01':'2016-01-31']
# dataMon2=greenPerformanceData.loc['2016-02-01':'2016-02-29']
# dataMon3=greenPerformanceData.loc['2016-03-01':'2016-03-31']
# dataMon4=greenPerformanceData.loc['2016-04-01']

print(dataMon1)
print(dataMon2)
print(dataMon3)
print(dataMon4)

dataMon1Group=dataMon1.groupby(['Service','Status of Order'], as_index=False).agg({'# of Orders':'sum','Total CBV':'sum'})
dataMon1Group.insert(loc=0,column='Month',value='1')
# print(dataMon1Group)
dataMon2Group=dataMon2.groupby(['Service','Status of Order'], as_index=False).agg({'# of Orders':'sum','Total CBV':'sum'})
dataMon2Group.insert(loc=0,column='Month',value='2')
# print(dataMon2Group)
dataMon3Group=dataMon3.groupby(['Service','Status of Order'], as_index=False).agg({'# of Orders':'sum','Total CBV':'sum'})
dataMon3Group.insert(loc=0,column='Month',value='3')
# print(dataMon3Group)
dataMon4Group=dataMon4.groupby(['Service','Status of Order'], as_index=False).agg({'# of Orders':'sum','Total CBV':'sum'})
dataMon4Group.insert(loc=0,column='Month',value='4')
# print(dataMon4Group)
dataMonthly=pd.concat([dataMon1Group,dataMon2Group,dataMon3Group,dataMon4Group])
print(dataMonthly)

# dfgui.show(dataMon1Group)
# dfgui.show(dataMon2Group)
# dfgui.show(dataMon3Group)
# dfgui.show(dataMon4Group)
dfgui.show(dataMonthly)