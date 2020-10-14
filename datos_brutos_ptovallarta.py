#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:49:25 2019

@author: leo
"""

import pandas as pd
import glob
import warnings



warnings.simplefilter(action='ignore', category=FutureWarning)

#pfrom = '/home/leo/Documents/delfin2019/rawdata/*'

pfrom = '/home/leo/Documents/tesis/Ptovallarta/cuc2.txt'

path2 = '/home/leo/Documents/tesis/ESIMES_SALIDAS/'#path archivos de salida

#path2 = '/home/leo/Documents/delfin2019/data/'#path archivos de salida

f1 =[]

for names in glob.glob(pfrom):
    
    #print(names)
    
    name = names.split('/')
    name = name[5]
    #name = name.replace('.txt','')
    
    pout = ''.join([path2, str(name) + '.csv'])
    print(pout)
    
#    pts1 = pd.read_csv(names, skiprows=1, usecols=['Date','Time','Out','wSpeed','wDir','Rain',
#                                       'Rad.'])

    #pts1 = pd.read_csv(names, header = None,sep='\t', skiprows=2, usecols=[0,1,2,5,7,8,16,17,19,22])
 
    pts1 = pd.read_csv(names, header = None,sep='\t', skiprows=2, usecols=[0,1,2,5,7,8,17,19])
    
    pts1 = pts1.replace({'---' : -99.9}, regex=True)
    pts1[1] = pts1[1].replace({'p' : 'pm'}, regex=True)
    pts1[1] = pts1[1].replace({'a' : 'am'}, regex=True)
    
    pts1['date'] = pts1[0].map(str) + '\t' + pts1[1]
    
    pts1['date'] = pd.to_datetime(pts1['date'], format='%d/%m/%y %I:%M %p')
    
    #if 
    
    #del pts1[0]
    #del pts1[1]
 
 #   for i in pts1[8]:
 #       if i=='S':
 #           pts1[8] = pts1[8].replace({'S' : 180}, regex=True)
 #       else:
 #           break
  

          
    #print(pts1[8])
    
    pts1[8] = pts1[8].replace({'N' : 0})
    pts1[8] = pts1[8].replace({'NNE' : 22.5})
    pts1[8] = pts1[8].replace({'NE' : 45})
    pts1[8] = pts1[8].replace({'ENE' : 67.5})
    pts1[8] = pts1[8].replace({'E' : 90})
    pts1[8] = pts1[8].replace({'ESE' : 112.5})
    pts1[8] = pts1[8].replace({'SE' : 135})
    pts1[8] = pts1[8].replace({'SSE' : 157.5})
    pts1[8] = pts1[8].replace({'S' : 180})
    pts1[8] = pts1[8].replace({'SSW' : 202.5})
    pts1[8] = pts1[8].replace({'SW' : 225})
    pts1[8] = pts1[8].replace({'WSW' : 247.5})
    pts1[8] = pts1[8].replace({'W' : 270})
    pts1[8] = pts1[8].replace({'WNW' : 292.5})
    pts1[8] = pts1[8].replace({'NW' : 315})
    pts1[8] = pts1[8].replace({'NNW' : 337.5})
    
    pst1 = pts1.fillna(-99.9)
    
    pts1[30] = pd.Series(77777, index=pts1.index)
    
    cols = pts1.columns.tolist()
    
    cols = [30,0,1,19,17,5,2,7,8,'date']
    
    pts1 = pts1[cols]
    
    #pts1 = pts1[[pst1[30],pst1[0]]]
    
    #print(cols)
    #print(pts1)
        
    #with open(pout, 'w') as f:
        
       # pts1.to_csv(f, header = ('TEMP', 'RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'), sep = '\t', index=False)
       
      # pts1.to_csv(f, sep = ' ', header = False, index=False)