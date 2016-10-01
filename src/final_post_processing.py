'''
Plot 

Created on 1 Oct 2016

@author: DefaultUser
'''

from pylab import scatter
import pylab
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def process_file(filename, variables_column_name, marker, label, selected_column):
    data1 = DataFrame(pd.read_csv(filename, delim_whitespace=True))
    
    gb1 = data1.groupby([variables_column_name]).mean()
    x= gb1.index.values
    y1 = gb1[selected_column]
    plt.scatter(x, y1, s=12, marker=marker, label = label)

def plot_all_for(type = 'time'):
    '''
    type: 'time' = time(s):
    type: 'HV' = HyperVolume
    '''
    type_of_plot = {'time':{
                            'ylabel':'Time(s)',
                            'title':'Variables - Time Scalability',
                            'column_name':'time(s):'
                            },
                    'HV':{
                          'ylabel':'Hypervolume',
                          'title':'Variables - Hypervolume Scalability',
                          'column_name':'HV'
                          }
                    
                    }
    
    f1 = 'all_tests_phd_corrections4_20000evals.txt'
    f2 = 'all_tests_phd_corrections5_20000evals.txt'
    f3 = 'all_tests_phd_corrections7_20000evals.txt'
    f4 = 'all_tests_phd_corrections6_20000evals.txt'
    f5 = 'all_tests_phd_corrections8_20000evals.txt'
    
    fig = plt.figure()
    
    process_file(f1, '#number_of_variables', "o", "case4_", type_of_plot[type]['column_name'])
    process_file(f2, '#nVar', "s", "case5_", type_of_plot[type]['column_name'])
    process_file(f3, '#nVar', "*", "case7_", type_of_plot[type]['column_name'])
    process_file(f4, '#nVar', "+", "case6_", type_of_plot[type]['column_name'])
    process_file(f5, '#nVar', ".", "case8_", type_of_plot[type]['column_name'])
    
    plt.xlabel('Number of variables')
    plt.ylabel(type_of_plot[type]['ylabel'])
    plt.gca().set_xscale('log')
    plt.title(type_of_plot[type]['title'])
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
    
# plot_all_for(type='time')
plot_all_for(type='HV')