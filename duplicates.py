#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:04:04 2020

@author: szatko
"""

def duplicates (sequence):
    list_of_dup = [] #creatinig empty list, to later on fill them up
    seq_list = []
    
    for i in sequence: #stripping string into list of characters
       seq_list.append(i) 
        
    while len(seq_list) > 1:
        #print (seq_list)
        for i in range(1, len(seq_list)):
            
            #print ("checked {0}, iterated {1}, ({2})".format(seq_list[0], seq_list[i], i))
            
            if seq_list[0] == seq_list[i]: #if found similar character i may add to list of duplicates
                list_of_dup.append(seq_list[i])
                seq_list.pop(0)
                break
            elif len(seq_list) != i + 1: #let function continue process of comaring
                continue
            else: #if dup has not ocurred, it may pop the chceked character
                seq_list.pop(0)
                break
    else: #finalizing the loop, counting number of duplicates, creating message
        
        #return (list_of_dup)
    
        message = "Found\n"
        temp = set(list_of_dup) #creating set to eliminate duplicates, to 
                                #obtain number of specyfic characters
        set_of_dup = list(temp) #returning to list, set does not support indexing
        #print(set(set_of_dup[1]))
        #print (list_of_dup, "\n", set_of_dup)
        
        
    
        for i in range(len(set_of_dup)): #creating message
            list_of_dup.count(set_of_dup[i-1])
            message += ("\"{0}\" {1} times\n".format(set_of_dup[i],list_of_dup.count(set_of_dup[i]) ))
            
        return print(message)

duplicates("ala ma kota")