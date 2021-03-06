'''
Plot 

Created on 1 Oct 2016

@author: DefaultUser

notes for Ipython:
    In [1]: %load_ext autoreload
    In [2]: %autoreload 2
    In [3]: from foo import some_function
    In [4]: some_function()
'''

from pylab import scatter
import pylab
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def process_file(case_specifications , selected_column):
    filename = case_specifications['filename']
    variables_column_name = case_specifications['variables_column_name']
    marker = case_specifications['mark']
    label = case_specifications["description"]
    data1 = DataFrame(pd.read_csv(filename, delim_whitespace=True))
    
    gb1 = data1.groupby([variables_column_name]).mean()
    x= gb1.index.values
    y1 = gb1[selected_column]
    plt.scatter(x, y1, s=12, marker=marker, label = label)

def plot_all_for(specifications_of_cases_to_compare, type = 'time', test_function_name="ZDT2"):
    '''
    type: 'time' = time(s):
    type: 'HV' = HyperVolume
    '''
    type_of_plot = {'time':{
                            'ylabel':'Elapsed Time(s)',
                            'title':'Variables - Elapsed Time Scalability',
                            'column_name':'time(s):',
                            'y_axis_range_min':-50,
                            'y_axis_range_max':400                            
                            },
                    'HV':{
                          'ylabel':'Hypervolume',
                          'title':'Variables - Hypervolume Scalability',
                          'column_name':'HV',
                          'y_axis_range_min':0,
                          'y_axis_range_max':6000,                          
                          }
                    
                    }
    
   
    
    fig = plt.figure()
    
    for filename in specifications_of_cases_to_compare:
        process_file(filename, type_of_plot[type]['column_name'])

    plt.xlabel('Number of variables')
    plt.ylabel(type_of_plot[type]['ylabel'])
    plt.gca().set_xscale('log')
    plt.title(type_of_plot[type]['title']+" for "+test_function_name)
    plt.grid(True)
    plt.legend(loc='upper left')
    
    plt.ylim(type_of_plot[type]['y_axis_range_min'], type_of_plot[type]['y_axis_range_max'])
    plt.show()
    
def plot_for_ZDT2():
#     f1 = {'filename':'all_tests_phd_corrections4_20000evals.txt', 'description':'nVar/5', 'mark':'o', 'variables_column_name':"#number_of_variables"}
    f2 = {'filename':'all_tests_phd_corrections5_20000evals.txt', 'description':'nVar/5', 'mark':'s', 'variables_column_name':"#nVar"}
    f3 = {'filename':'all_tests_phd_corrections7_20000evals.txt', 'description':'nVar/9', 'mark':'*', 'variables_column_name':"#nVar"}
    f4 = {'filename':'all_tests_phd_corrections6_20000evals.txt', 'description':'nVar/11', 'mark':'+', 'variables_column_name':"#nVar"}
    f5 = {'filename':'all_tests_phd_corrections8_20000evals.txt', 'description':'nVar/13', 'mark':'.', 'variables_column_name':"#nVar"}
    
    specifications_of_cases_to_compare_for_ZDT2 =[ f2, f3, f4, f5]
    plot_all_for(type='time', test_function_name="ZDT2", specifications_of_cases_to_compare=specifications_of_cases_to_compare_for_ZDT2)
    plot_all_for(type='HV', test_function_name="ZDT2", specifications_of_cases_to_compare=specifications_of_cases_to_compare_for_ZDT2)
    
def plot_for_ZDT1():
#     f1 = {'filename':'all_tests_phd_corrections10b_zdt1_20000evals.txt', 'description':'nVar/13a', 'mark':'o', 'variables_column_name':"#nVar"}
    f5 = {'filename':'all_tests_phd_corrections13_zdt1_20000evals.txt', 'description':'nVar/5', 'mark':'s', 'variables_column_name':"#nVar"}
    f4 = {'filename':'all_tests_phd_corrections12_zdt1_20000evals.txt', 'description':'nVar/9', 'mark':'*', 'variables_column_name':"#nVar"}
    f3 = {'filename':'all_tests_phd_corrections11_zdt1_20000evals.txt', 'description':'nVar/11', 'mark':'+', 'variables_column_name':"#nVar"}
    f2 = {'filename':'all_tests_phd_corrections10e_zdt1_20000evals.txt', 'description':'nVar/13', 'mark':'.', 'variables_column_name':"#nVar"}

    specifications_of_cases_to_compare_for_ZDT1 =[f5, f4, f3, f2]
    plot_all_for(type='time', test_function_name="ZDT1", specifications_of_cases_to_compare=specifications_of_cases_to_compare_for_ZDT1)
    plot_all_for(type='HV', test_function_name="ZDT1", specifications_of_cases_to_compare=specifications_of_cases_to_compare_for_ZDT1)

plot_for_ZDT2()
    