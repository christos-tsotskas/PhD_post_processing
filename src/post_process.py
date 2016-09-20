'''
Created on 19 Sep 2016

@author: Christos
'''
import numpy as np
import matplotlib.pyplot as plt

class Visualiser(object):
    
    __data = None
    __filename_to_plot = None
    __name = None
    __figure_number = None
    __figure = None
    
    def __init__(self, filename_to_plot, name, figure_number):
        self.__filename_to_plot = filename_to_plot
        self.__name = name
        self.__figure_number = figure_number
   
        


    def load_file_to_data_structure(self):
        '''
        expects data with 3 columns, where 
            the first column is the number of variables
            the second column is the time the optimisation run
            the third column is the Hypervolume indicator (calculated from 20,20)
        '''
        with open(self.__filename_to_plot) as in_file:
            lines = [line.rstrip('\n') for line in in_file]
            if lines[0].startswith("#"):
                lines.pop(0)
    
            number_of_lines = len(lines)
#             self.__data = np.empty([number_of_lines, 3], dtype=float)
            self.__data = np.zeros(shape=(number_of_lines, 3), dtype=float)
    
            row_index = 0
            for line in lines:
                text = line.split()

                self.__data[row_index][0] = float(text[0])
                self.__data[row_index][1] = float(text[1])
                self.__data[row_index][2] = float(text[2])            
                row_index += 1
            

            
    def plot_two_axis_of_the_same_case(self):
        number_of_variables = self.__data[:,0]
        time_performance = self.__data[:,1]
        HV_performance = self.__data[:,2]       
        
        plt.figure(self.__figure_number)
        fig, ax1 = plt.subplots()
        
        ax1.set_title('Scalability of '+self.__name)
        ax1.semilogx(number_of_variables, time_performance, '.')
        ax1.set_xlabel('Number of variables')
        
        # Make the time_performance-axis label and tick labels match the line color.
        ax1.set_ylabel('Time(s)', color='b')
        for tl in ax1.get_yticklabels():
            tl.set_color('b')        
        
        ax2 = ax1.twinx()       
        ax2.semilogx(number_of_variables, HV_performance, '*')
        ax2.set_ylabel('HV indicator', color='r')
        for tl in ax2.get_yticklabels():
            tl.set_color('r')


    def plot_comparisons(self):
        pass

    def test1(self):
        self.load_file_to_data_structure()         
        self.plot_two_axis_of_the_same_case()


if __name__ == '__main__':
    f1 = 'all_tests_phd_corrections4_20000evals.txt'
    f2 = 'all_tests_phd_corrections5_20000evals.txt'
    f3 = 'all_tests_phd_corrections7_20000evals.txt'
    

    v1 = Visualiser(f2,'case5',1)
    v1.test1()    
    
    v2 = Visualiser(f3,'case7',2)
    v2.test1()

    v3 = Visualiser(f1,'case4',3)
    v3.test1()    

    plt.show()

#     plt.show()