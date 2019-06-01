#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:24:20 2019

@author: carlos
"""

import os
import time
import numpy as np
import shutil

path='/home/carlos/Documentos/FeF/Ejercicios_primera_clase/Fotis/'
archivos=os.listdir(path)

tiempos=[]
for i in archivos:
    tiempos.append(time.gmtime(os.path.getmtime(path+i)))
    #getctime levanta la fecha de reación de un arhivo expresaa en segundos desde
    #la creación del sistema operativo
    #time.gmetime convierte ese tiempo a una tupla que expresa año,mes,día y así

anos=[]
meses=[]
dias=[]

for i in tiempos:
    anos.append(i[0])
    meses.append(i[1])
    dias.append(i[2])

anos=np.array(anos)
meses=np.array(meses)
dias=np.array(dias)

for i in range(0,len(anos)):
    os.makedirs(path+str(dias[i])+'-'+str(meses[i])+'-'+str(anos[i]),exist_ok=True)
    
for i in range(0,len(archivos)):    
     shutil.move(path+archivos[i], path+str(dias[i])+'-'+str(meses[i])+'-'+str(anos[i]))
    
#Holaaaaaaaaa222222