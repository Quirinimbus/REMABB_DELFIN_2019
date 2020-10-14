#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:50:39 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

datain = '/home/leo/Documents/delfin2019/data/*'

metadata = '/home/leo/Documents/delfin2019/metadata/'

for ID in glob.glob(datain):
    
    #print(ID)
    
    METAID = ID.split('/')
    METAID = METAID[6]
    METAID = METAID.replace('.csv','')
    
    metaout = ''.join([metadata, str(METAID) + '.csv'])
    #print(metaout)
    
    DF0 = pd.read_csv(ID, sep = '\t')#, names=['Temp','RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'])
    
    df = pd.DataFrame(DF0)#, columns=['Temp','RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'])
    
    #print(df['PP'])
    
#################################################################################

################   BASE DATOS

################################################################################# 
    
    df1 = df[(df.TEMP > 4) & (df.TEMP < 40)] # temperatura

    df2 = df[(df.SR > 0) & (df.SR < 1400)] # rad solar

    df3 = df[(df.RH > 4) & (df.RH < 101)] # hum relativa

    df4 = df[(df.PP >= 0) & (df.PP < 16)] # preciptación
    
    df5 = df[(df.WS >= 0) & (df.WS < 16)] # viento velocidad
    
    
    
    #df.loc[:, (df.TEMP>= 5) & (df.TEMP<=-41)] = np.nan
    
    #df['TEMP'] = df[(df.TEMP > 4) & (df.TEMP < 40)] # temperatura

    #df['SR'] = df[(df.SR > 0) & (df.SR < 1400)] # rad solar

    #df['RH'] = df[(df.RH > 4) & (df.RH < 101)] # hum relativa

    #df['PP'] = df[(df.PP >= 0) & (df.PP < 16)] # preciptación
    
    #df['WS'] = df[(df.WS >= 0) & (df.WS < 16)] # viento velocidad
    
    #print(df)
    
    metadf = ''.join([metadata, 'METAESTACIONES/' + str(METAID) + '.csv'])
    
    df.to_csv(metadf, index=False,  sep = '\t')
    
#################################################################################

################   Temp

#################################################################################     


    dftn =  pd.DataFrame(data = df1, columns = ['DATE', 'TEMP'])
    
    metatemp = ''.join([metadata, 'TEMP/' + str(METAID) + '.csv'])
    
    #print(metatemp)
    
    dftn.to_csv(metatemp, index=False,  sep = '\t')
    
    #print(dftn)

#################################################################################

################   SOLAR RAD

#################################################################################     


    dfsr =  pd.DataFrame(data = df2, columns = ['DATE', 'SR'])
    
    metasr = ''.join([metadata, 'SOLARRAD/' + str(METAID) + '.csv'])
    
    #print(metasr)
    
    dfsr.to_csv(metasr, index=False,  sep = '\t')
    
    #print(dfsr)
    
    
#################################################################################

################   HUM RELATIVA

#################################################################################     


    dfrh =  pd.DataFrame(data = df3, columns = ['DATE', 'RH'])
    
    metarh = ''.join([metadata, 'HUMRELATIVA/' + str(METAID) + '.csv'])
    
    #print(metarh)
    
    dfrh.to_csv(metarh, index=False,  sep = '\t')
    
   # print(dfrh['RH'].max())
    
    
#################################################################################

################   PRECIPITACIÓN

#################################################################################     


    dfpp =  pd.DataFrame(data = df4, columns = ['DATE', 'PP'])
    
    metapp = ''.join([metadata, 'PRECIPITACION/' + str(METAID) + '.csv'])
    
    #print(metapp)
    
    dfpp.to_csv(metapp, index=False,  sep = '\t')
    
    #print(dfpp['PP'].max())

    
#################################################################################

################   Viento

################################################################################# 
    
    dfws =  pd.DataFrame(data = df5, columns = ['DATE','WS','WD'])
    
    metaws = ''.join([metadata, 'VIENTO/' + str(METAID) + '.csv'])
    
    #print(metaws)
    
    dfws.to_csv(metaws, index=False, sep = '\t')
    
    #print(dfws['WS'].max())