# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:45:52 2022

@author: youssef
"""

def fct(x):
    return x-2

eps=0.001

a = int(input ("Entrer a  "))
b = int(input ("Entrer b  "))

while(fct(a)*fct(b)>=0) :
    a = int(input ("Entrer a  "))
    b = int(input ("Entrer b  "))
    
it = 0
f2 = 0
f0 = fct(a)
print("a = ",a)
print("b = ",b)

while ((b-a)/2>eps) :
    c=(a+b)/2
    f2=fct(c)
    if f0 * f2 < 0 :
        b = c
    else :
        a = c
        f0 = f2
        it=it+1
        
print("le zero est : ",c)
print(" le nbr d'iteration ",it)
        

