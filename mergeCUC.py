#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:54:54 2019

@author: leo
"""

import pandas as pd
import glob

pCUC2 = '/home/leo/Documents/delfin2019/data/cuc2.csv'

pCUC1 = '/home/leo/Documents/delfin2019/data/cuc1.csv'

outCUC = '/home/leo/Documents/delfin2019/data/cuc.csv'

#result = df1.append(df4, sort=False)

cuc2 = pd.read_csv(pCUC2,  sep = '\t')

CUC2 = pd.DataFrame(data=cuc2, columns = ['TEMP', 'RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'])

#print(CUC2)

cuc1 = pd.read_csv(pCUC1,  sep = '\t')

CUC1 = pd.DataFrame(data=cuc1, columns = ['TEMP', 'RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'])

CUC = CUC1.combine_first(CUC2)

CUC = CUC.fillna('NA')

print(CUC)

with open(outCUC, 'w') as f1:
        
    CUC.to_csv(f1, header = ('TEMP', 'RH','WS','WD','PBAR','PP','SR','UVIDX','DATE'), sep = '\t', index=False)