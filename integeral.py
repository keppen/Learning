#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:57:51 2020

@author: szatko
"""
def integral (beggining, end): #lets start with prefixed equation
    
    resolution = (end - beggining) / 100000# establishing resolution to have dletax
    sum = 0                         #definig var in advance
    while (beggining + resolution) <= end:
        equation1 = beggining**2
        equation2 = (beggining + resolution)**2
        '''
        debug purposess
        
        print ("arguent1 =", beggining, "argunet2 =", beggining + resolution)
        print ("eq1 =", equation1, "eq2=", equation2)
        '''
        sum += (equation1 + equation2)/2 * resolution #trapezoid rule - usdes method to calculate intergal
        beggining += resolution                 #changing deltax
        
        #print ("sum=", sum, end= "\n \n")
        
    else:
        resolution = end - beggining #need to recalculate deltax for last two argumennts
        equation1 = beggining**2
        equation2 = end**2
        
        sum += (equation1 + equation2)/2 * resolution
        
        #print ("prelast argument=", beggining, "last argument =", end, "\n final sum=", sum)
        
        return print(sum)  

integral(0, 0.01)
'''
just need to have working function


x = 1 #have to define x var
eq1 = x**2 #to have sth to work on
'''

