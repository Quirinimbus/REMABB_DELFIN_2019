#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:27:41 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

#metain = '/home/leo/Documents/delfin2019/metadata/METAESTACIONES/*'

datain = '/home/leo/Documents/delfin2019/data/*'

producto = '/home/leo/Documents/delfin2019/'

#print(metain)
from datetime import datetime



for IDX in glob.glob(datain):
    
    #print(IDX)

    file1 = (open(IDX))
    next(file1)
    f0 = file1.readlines()
    file1.close
    f1 = []

    STID = IDX.split('/')
    STID = STID[6]
    STID = STID.replace('.csv','')
    
    out = ''.join([producto, str(STID) + '.csv'])
    #print(f1)
    
    
    
    for i in range(len(f0)):
        
        #print(i)
        
        tmpln = f0[i]
        
        tmpln = tmpln.replace('NA', '-99.9')
        
        tn, rh, ws, wd, pr, pp, sr, uv, time = tmpln.split('\t',9)
        
        #print(sr)
        #ID, time0, x0, time = tmpln.split('"',3)
         
        time = time.replace(' ','\t')

        time = time.replace('-','\t')
        
        time = time.replace(':','\t')
        
        time = time.replace('\n','')
        
        #print(tmpln[1])
        
        #print(time)
        
        tmpln0 = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(time, tn, rh, ws, wd, pr, pp, sr, uv)
                                
        f1.append(tmpln0)
    
    f1='\n'.join(f1)
    
    df = pd.read_csv(StringIO(f1), sep = '\t', header = None,
                      names=['aa','mm','dd','hr','mn','sc', 'tn', 'rh', 'ws', 'wd', 'pr', 'pp', 'sr', 'uv'])#, names=['Temp','RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'])
    
    df = df.fillna(np.nan)
    
    d1 = datetime(df['aa'].iloc[0], df['mm'].iloc[0], df['dd'].iloc[0], df['hr'].iloc[0], df['mm'].iloc[0], 0)
    d2 = datetime(df['aa'].iloc[-1:], df['mm'].iloc[-1:], df['dd'].iloc[0], df['hr'].iloc[0], df['mm'].iloc[0], 0)
    di = d2 - d1
    print (di)
    
    n0 = len(df)
    
    ntotal = di*24*6
    
    #print(ntotal)
    
    #print(df['aa'].iloc[0])
    
    #print(len(df))
    
    print(df['aa'].iloc[-1:])
    
    fig001, ax001 = plt.subplots()
    ax001.set_title('Temp sin filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax001.boxplot(df['tn'])#,xlab="Temp", ylab="C")
    
    plottmpsin = '/'.join([producto,'plots/temp' + str(STID) + 'sin.png'])
    
    plt.savefig(plottmpsin)

    plt.show()
    
    fig002, ax002 = plt.subplots()
    ax002.set_title('Humedad Relativa sin filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax002.boxplot(df['rh'])#,xlab="Temp", ylab="C")  
    
    plotrhsin = '/'.join([producto,'plots/rh' + str(STID) + 'sin.png'])
    
    plt.savefig(plotrhsin)

    plt.show()
    
    fig003, ax003 = plt.subplots()
    ax003.set_title('Radiación Solar sin filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax003.boxplot(df['sr'])#,xlab="Temp", ylab="C")
    
    plotsrsin = '/'.join([producto,'plots/sr' + str(STID) + 'sin.png'])
    
    plt.savefig(plotsrsin)

    plt.show()
    
    fig004, ax004 = plt.subplots()
    ax004.set_title('Precipitación sin filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax004.boxplot(df['pp'])
    
    plotppsin = '/'.join([producto,'plots/pp' + str(STID) + 'sin.png'])
    
    plt.savefig(plotppsin)

    plt.show()
    
    fig005, ax005 = plt.subplots()
    ax005.set_title('Viento sin filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax005.boxplot(df['ws'])
    
    plotwssin = '/'.join([producto,'plots/ws' + str(STID) + 'sin.png'])
    
    plt.savefig(plotwssin)

    plt.show()
    
#################################################################################

################   BASE DATOS

################################################################################# 
    
    df1 = df[(df.tn > 4) & (df.tn < 40)] # temperatura
    
    n1 = len(df1)
    
    t100 = n1/n0
    t100 = np.round(t100, decimals=4)

    df2 = df[(df.sr > 0) & (df.sr < 1400)] # rad solar

    n2 = len(df2)
    sr100 =n2/n0
    sr100 = np.round(sr100, decimals=4)

    df3 = df[(df.rh > 4) & (df.rh < 101)] # hum relativa

    n3 = len(df3)
    rh100 = n3/n0
    rh100 = np.round(rh100, decimals=4)

    df4 = df[(df.pp >= 0) & (df.pp < 16)] # preciptación
    print(df4['pp'].max())
    
    n4 = len(df4)
    pp100 = n4/n0
    pp100 = np.round(pp100, decimals=4)
    
    df5 = df[(df.ws >= 0) & (df.ws < 16)] # viento velocidad
    
    n5 = len(df5)
    ws100 = n5/n0
    ws100 = np.round(ws100, decimals=4)
    
    print(ws100)
    
    fig101, ax101 = plt.subplots()
    ax101.set_title('Temp con filtro ' + STID)
    ax101.boxplot(df1['tn'])
    
    plottmpcon = '/'.join([producto,'plots/temp' + str(STID) + 'con.png'])
    
    plt.savefig(plottmpcon)

    plt.show()
    
    fig102, ax102 = plt.subplots()
    ax102.set_title('Humedad Relativa con filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax102.boxplot(df3['rh'])#,xlab="Temp", ylab="C")  
    
    plotrhcon = '/'.join([producto,'plots/rh' + str(STID) + 'con.png'])
    
    plt.savefig(plotrhcon)

    plt.show()
    
    fig103, ax103 = plt.subplots()
    ax103.set_title('Radiación Solar con filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax103.boxplot(df2['sr'])#,xlab="Temp", ylab="C")  
    
    plotsrcon = '/'.join([producto,'plots/sr' + str(STID) + 'con.png'])
    
    plt.savefig(plotsrcon)

    plt.show()
    
    fig104, ax104 = plt.subplots()
    ax104.set_title('Precipitación con filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax104.boxplot(df4['pp'])#,xlab="Temp", ylab="C") 
    
    plotppcon = '/'.join([producto,'plots/pp' + str(STID) + 'con.png'])
    
    plt.savefig(plotppcon)

    plt.show()
    
    fig105, ax105 = plt.subplots()
    ax105.set_title('Viento con filtro ' + STID)
    #ax1.ylabel('Aspect (1-deg bins)')
    ax105.boxplot(df5['ws'])#,xlab="Temp", ylab="C") 
    
    plotwscon = '/'.join([producto,'plots/ws' + str(STID) + 'con.png'])
    
    plt.savefig(plotwscon)

    plt.show()
    
    
    table01 = '{},{},{},{},{},{},{},{}\n'.format(STID,d1,d2,t100,rh100,sr100,pp100,ws100)
    
    pathtable = ''.join([producto,'table/'+ 'descripcion.csv'])
    with open(pathtable, 'a') as file10:
        file10.write(table01)
        
        #table01.to_csv(file10, header = False , sep = ' ',index=False, na_rep = np.nan)
    
    
    
    print(table01)
    
###############################################################################
######           Temperatura Ambiente
###############################################################################

    dftn = pd.DataFrame(data = df1, columns = ['aa', 'mm', 'dd','hr','mn','tn'])
    dftn = dftn[np.abs(dftn.tn-dftn.tn.mean())<=(3*dftn.tn.std())] # Elimina valores > |3 desviaciones estándares| 

    tnmean = dftn.groupby(['mm'], as_index=False)['tn'].mean()
    tnmean = np.round(tnmean, decimals=1)

    tnmax = dftn.groupby(['mm','hr'], as_index=False)['tn'].max()
    tnmaxmean = tnmax.groupby(['mm'], as_index=False)['tn'].mean()
    tnmaxmean = np.round(tnmaxmean, decimals=1)

    tnmin = dftn.groupby(['mm','hr'], as_index=False)['tn'].min()
    tnminmean = tnmin.groupby(['mm'], as_index=False)['tn'].mean()
    tnminmean = np.round(tnminmean, decimals=1)

    tnhora = dftn.groupby(['mm','hr'], as_index=False)['tn'].mean()
    tnhora = np.round(tnhora, decimals=1)
    
    TN =  pd.merge(tnmaxmean, tnminmean, on = ['mm'])

    DFTN = pd.merge(tnmean, TN, on = ['mm'])

    #ax2 = plt.gca()
    #ax2.set_xticks(DFTN['mm'], minor=False)
    #ax2.set_xlim(1,12)
    #ax2.set_ylim(0,45)
    
    #DFTN.plot(kind='line',x='mm', y='tn_x', color = 'red', ax=ax2, label='$T_{max}$')
    #DFTN.plot(kind='line',x='mm', y='tn', color = 'black', ax=ax2, label='$T$')
    #DFTN.plot(kind='line',x='mm',y='tn_y', color='blue', ax=ax2, label='$T_{min}$')

    #plt.fill_between(DFTN['mm'],DFTN['tn_y'],DFTN['tn_x'], facecolor='silver', alpha=0.6)
    #ax2.set_xlabel('Mes')
    #ax2.set_ylabel('Temp (°C)')
    #ax2.set_title('Temperaturas Promedio ' + str(STID))
    #ax2.grid(True, linestyle='--')
    
    #plt.show()
    
###############################################################################
######           Precipitación
###############################################################################

    dfpp = pd.DataFrame(data = df4, columns = ['aa', 'mm', 'dd','hr','mn','pp'])

    #ppmeanhr =  dfpp.groupby(['aa','mm','dd','hr'], as_index=False)['pp'].mean()
    #ppmeanhr = np.round(ppmeanhr, decimals=1)
    
    #df5 = ppmeanhr[(ppmeanhr.pp > 0) & (ppmeanhr.pp < 100)]
    
    ppaasum = df4.groupby(['aa','mm'], as_index=False)['pp'].sum()
    ppaasum = np.round(ppaasum, decimals=1)
    
    #print(ppaasum)
    
    ppmean = ppaasum.groupby(['mm'], as_index=False)['pp'].mean()
    ppmean = np.round(ppmean, decimals=1)
    
    PP0 =  pd.merge(ppmean, tnmean, how = 'outer' ,on = ['mm'])
    
    #print(PP0)
    
    #Precip = '/'.join([p2,'Precip/' + str(estacion) + '.csv'])
    
    #PP0.to_csv(Precip, index=False, header = False, sep = ' ')
   
    ppmax = ppmean.max()
    
    #ax2 = plt.gca()
    #ax2.set_xticks(dftn['mm'], minor=False)
    #ax2.set_xlim(1,12)
    #ax2.set_ylim(0,40)
    
    #df = pd.DataFrame(DF0
    
###############################################################################
######           Índice Ombrotérmico
###############################################################################
    T = tnmean['tn']
    PP = ppmean['pp']

    OT1 = (PP/(2*T)) - 1 #Propuesta por Gómez Azpeitia
    
    #print('OT1 =', len(OT1))

    #fig, ax4 = plt.subplots()

    #ax5 = ax4.twinx()
    #ax4.plot(T, 'red')
    
    #ax5.plot(DFTN['mm'], PP, 'blue')
    #ax4.set_xticks(DFTN['mm'], minor=False)
    #ax4.set_xlim(1,12)

    #ax4.set_ylim(0,ppmax['pp']/2)

    #PP.plot(kind='bar', x='mm', y='pp', color = 'blue', ax=ax5, label='$PP$')

    #ax4.set_xlabel('Mes')
    #ax4.set_ylabel('Temp (°C)')
    #ax4.set_title('Ombrotérmico ' + str(STID))
    #ax4.grid(True, linestyle='--')
    #ax5.set_ylabel('mm')

    #plotOH1 = '/'.join([p2,'Ombrotermico/plotOH1' + str(estacion) + '.png'])

    #plt.savefig(plotOH1)
    
    #plt.show()