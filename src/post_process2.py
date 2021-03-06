'''
Created on 26 Sep 2016

@author: DefaultUser
'''

from pylab import scatter
import pylab
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def plot_quality():
    f1 = 'all_tests_phd_corrections4_20000evals.txt'
    f2 = 'all_tests_phd_corrections5_20000evals.txt'
    f3 = 'all_tests_phd_corrections7_20000evals.txt'
    f4 = 'all_tests_phd_corrections6_20000evals.txt'
    f5 = 'all_tests_phd_corrections8_20000evals.txt'
    
    all_files = [f1, f2, f3, f4, f5]
    
    data1 = DataFrame(pd.read_csv(f1, delim_whitespace=True))    
    data2 = DataFrame(pd.read_csv(f2, delim_whitespace=True))
    data3 = DataFrame(pd.read_csv(f3, delim_whitespace=True))
    data4 = DataFrame(pd.read_csv(f4, delim_whitespace=True))    
    data5 = DataFrame(pd.read_csv(f5, delim_whitespace=True))
#     data2 = DataFrame(pd.read_csv(f2))
#     data3 = DataFrame(pd.read_csv(f3))
    
        
    x1 = np.array(data1['#number_of_variables'], dtype='int')
    y1 = np.array(data1['time(s)'], dtype='float32') 
    
    x2 = np.array(data2['#nVar'], dtype='int')
    y2 = np.array(data2['time(s):'], dtype='float32')
     
    x3 = np.array(data3['#nVar'], dtype='int')
    y3 = np.array(data3['time(s):'], dtype='float32')
    
    x4 = np.array(data4['#nVar'], dtype='int')
    y4 = np.array(data4['time(s):'], dtype='float32')
    
    x5 = np.array(data5['#nVar'], dtype='int')
    y5 = np.array(data5['time(s):'], dtype='float32')
    
    fig = plt.figure()
    plt.scatter(x1, y1, s=10, c='r', marker="o", label = 'case4')
    plt.scatter(x2, y2, s=13, c='b', marker="s", label = 'case5')
    plt.scatter(x3, y3,  marker="*",  label = 'case6')
    plt.scatter(x4, y4,  marker="+",  label = 'case7')
    plt.scatter(x5, y5,  marker=".",  label = 'case8')
    
   #markers: ',', '+', '.', 'o', '*'
        
    plt.xlabel('Number of variables')
    plt.ylabel('Time(s)')
    plt.title('Variables - Time Scalability')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
    
if __name__ == "__main__":
    plot_quality()