'''
Created on 19 Sep 2016

@author: Christos
'''
import numpy as np
import matplotlib.pyplot as plt

class Visualiser(object):
    
    __data = None
    
    def __init__(self):
        pass

    def load_file_to_data_structure(self, filename):
        '''
        expects data with 3 columns, where 
            the first column is the number of variables
            the second column is the time the optimisation run
            the third column is the Hypervolume indicator (calculated from 20,20)
        '''
        with open(filename) as in_file:
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
            

            
    def plot_data(self):
        number_of_variables = self.__data[:,0]
        time_performance = self.__data[:,1]
        HV_performance = self.__data[:,2]
        
        
        
        fig, ax1 = plt.subplots()
        
        ax1.set_title('Scalability')
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
        plt.show()

#         plt.semilogx(number_of_variables,time_performance,'.' )
#         plt.xlabel('Number of variables')
#         plt.ylabel('Time(s)')
#         plt.grid(True)
#         plt.show()
    
    def test1(self):
        data1 = self.load_file_to_data_structure('test2.txt')
        print 
        self.plot_data()
        

if __name__ == '__main__':
    v1 = Visualiser()
    v1.test1()