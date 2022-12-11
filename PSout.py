#-------------------------------------------------------------------------------
# Name:        pscaduc.py
# Purpose:     Python Package for PSCAD automation
#
# Author:      Mario Mañana Canteli
#
# Created:     20/04/2021
# Copyright:   (c) mananam 2021
# Licence:     GNU v3
#-------------------------------------------------------------------------------

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Print version of Python compiler
#print( sys.version)
#print( sys.executable)
#print('*************************************************')

class PSout:
    
    def __init__(self):
        self.version = r"v1.0"
        
    
    def out_avg( self, path, file_out, file_inf, signal, Navg):
    # Path of the out file
    #path = r'E:\mario\docencia\Simulacion de sistemas electricos\emtp\python_scripting\capacitiva_01.gf46'
    #file_out = r'\capacitiva_1_01.out'
    #file_inf = r'\capacitiva_1.inf'
    # Signal
    #signal = r'"RT_1"'
    # Navg
    #Navg = 100
        f_out = path + file_out
        f_inf = path + file_inf

        #print(r'Output file')
        #print( f_out)
        #print(r'Information file')
        #print( f_inf)
        #print(r'Signal')
        #print( signal)

        # Read file line by line
        finfo = open( f_inf, 'r')
        Linfo = finfo.readlines()

        count = 0
        for line in Linfo:
            count += 1
            # find PGB(
            index = line.find( 'PGB(')
            if index != -1:
                ch = line[index+4]
                # print( ch)
                index = line.find( signal)
            if index != -1:
                channel = int(ch)
                #print( 'canal: ' + str(channel))

        Nc = count+1

        data = pd.read_csv(
                    f_out,
                    delimiter=r"\s+",
                    skiprows = 1
                    )


        ColNames = []
        for i in range(Nc):
            label = 'C' + str(i)
            ColNames.append( label)

        data.columns = ColNames

        A = data[ ColNames[ channel]]
        N = len(A)

        AVG = np.average( A[N-Navg:N-1])
        #print(str(AVG))

        return( AVG)
