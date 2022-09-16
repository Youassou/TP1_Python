# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:14:50 2022

@author: youssef
"""
import numpy as np
import matplotlib.pyplot as plt

import math
def fct(x):
    return x-2

eps=0.001
i=0
EPS=0
t=0
a=0
b=0
c=0
f1=0
f2 = 0

a = int(input ("Entrer a  "))
b = int(input ("Entrer b  "))

while True :
    i=i+1
    f1=fct(a)
    f2=fct(b)
    c = b - ((f2*(b-a))/(f2-f1))
    a=b
    b=c
    if(f2<0):
        t=math.fabs(f2);
    else :
        t=f2;
    if(t<eps):
        break
    
print("Le zero de la fct est : ",c)
print("Le nbr d'iteration est : ",i)

