import numpy as np
import pandas as pd
import math
from collections import Counter



def trim_mean(data, trim_percent):

    trimVals = round(trim_percent * len(data))

    if trimVals == 0:
        return sum(data)/len(data)

    trimlst =data[trimVals:-trimVals]
    if trimlst ==0:
        return

    trimAvg = sum(trimlst) / len(trimlst)

    return trimAvg


def geo_mean(data):
    m=1

    for i in range(0,len(data)):
        m =m*data[i]
    if m < 0:
        m = m*(-1)
    geoAvg = (float)(math.pow(m, (1/len(data))))
    t = (float)(geoAvg)
    return t

def har_mean (data):
    s=0
    for i in data:
        s += (1/i)
    harAvg = len(data)/s
    return harAvg

def median (data):

    n = len(data)//2

    if n%2 ==0:
        med = (sum(data[n-1:n]))/2
    
    else:
        med = data[n]
    return med

def mymode (data):

    n = len(data)
    data_num = Counter(data)
    get_mode = dict(data_num)
    mode = [k for k, v in get_mode.items() if v == max(list(data_num.values()))]

    if len(mode) == n:
        get_mode = "No mode found"
    elif len(mode)==1:
        get_mode = "Mode is  " + 'UNIMODAL ' + ', '.join(map(str, mode))
    elif len(mode)== 2:
        get_mode = "\nMode are: " + 'BIMODAL '+ ', '.join(map(str, mode))
    else:
        get_mode = '\nMode  are: ' + 'MULTIMODAL '+ ', '.join(map(str, mode))

    print(get_mode)


if __name__ == '__main__':

    dataset = pd.read_excel('diamond price.xlsx')
    dataset_list = dataset['price'].tolist()
    dataset_list.sort()

    NumVals=len(dataset_list)
    print('\nNumber of Values  is: ' + str(NumVals))

    MaxVal= dataset_list[-1]
    print('\nMaximum Value  is: ' + str(MaxVal))

    MinVal = dataset_list[0]
    print('\nminimum Value  is: ' + str(MinVal))

    Mean = sum(dataset_list)/len(dataset_list)
    print('\nMean  is: ' + str(Mean))

    TenPercentTrimmedMean = trim_mean(dataset_list,0.1)
    print('\n10% Trimmed Mean  is: ' + str(TenPercentTrimmedMean))

    TwentPercentTrimmedMean = trim_mean(dataset_list, 0.2)
    print('\n20% Trimmed Mean  is: ' + str(TwentPercentTrimmedMean))

    GeoMean = geo_mean(dataset_list)
    print('\nGeometric Mean  is: ' + str(GeoMean))

    HarMean = har_mean(dataset_list)
    print('\nHarmonic Mean  is: ' + str(HarMean))

    Median = median(dataset_list)
    print('\nMeadian  is: ' + str(Median))

    MidRange = (MaxVal + MinVal)/2
    print('\nMidrange  is: ' + str(MidRange))

    Mode = mymode(dataset_list)
   

    
