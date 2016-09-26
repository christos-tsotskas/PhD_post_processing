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
    
    data1 = DataFrame(pd.read_csv(f1, delim_whitespace=True))
    
    
    
    exit
    data2 = DataFrame(pd.read_csv(f2, delim_whitespace=True))
#     data2 = DataFrame(pd.read_csv(f2))
#     data3 = DataFrame(pd.read_csv(f3))
    
        
    x1 = np.array(data1['#number_of_variables'], dtype='int')
    y1 = np.array(data1['time(s)'], dtype='float32')
    
 
    
    x2 = np.array(data2['#nVar'], dtype='int')
    y2 = np.array(data2['time(s):'], dtype='float32')
     

    
    fig = plt.figure()
    plt.scatter(x1, y1, s=10, c='r', marker="o", label = 'case4')
    plt.scatter(x2, y2, s=10, c='b', marker="s", label = 'case5')
    
    plt.xlabel('Number of variables')
    plt.ylabel('Time(s)')
    plt.title('Variables - Time Scalability')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
    
if __name__ == "__main__":
    plot_quality()