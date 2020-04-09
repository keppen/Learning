#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:05:36 2020

@author: szatko
"""
import copy
import random


def game_of_life(plane, v, h, cycles): # check if v and h arg are needed
    new_plane = []
    
    if cycles == 0:
        
#to avoid complex introducing complex border conditions, matrix has 2 extra vertical and horizontal rows
# and there is one empty nested list , p, its excluded from iterating eathier

        return ('\n finished') 
    
    
    else:
        
        print ('\ncycle ', cycles, '\n')
        
        new_plane = copy.deepcopy(plane) # first need to apply the rules to the plane, then make new one
    
        for i in range ( 2, v ): # iterating within a matrix
        
            for j in range ( 1 , h - 1):
        
                count = 0 
            
            
            
                for r in range (-1, 2, 1): #checking surondings of an intem
                    if r == 0:
                
                        for p in range (-1, 2, 2): #do not count checked cell itself
                        
                            if plane[i + r][j + p] == 0:
                                count += 1
                        
                            else:
                                continue
                    else:
                        for p in range (-1, 2, 1):
                        
                            if plane[i + r][j + p] == 0:
                                count += 1
                        
                            else:
                                continue
                        
                        
                        
                if plane[i][j] ==  1: # applying chaneg in regard to rules
                
                    if count == 3:
                        new_plane[i][j] = 0
                    
                    else:
                        continue
                else:
                
                    if count < 2 or count > 3:
                        new_plane[i][j] = 1
                
                    else:
                        continue
    
    
        for i in range(len(new_plane) - 3): #making matrix more readable
            print (new_plane[i + 2][1:-1] ) 
        
        return (game_of_life(new_plane, vertical, horizontal, cycles - 1)) 
        #for sake of cycles need to invoke funciotn number of times    

#OkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDoki

def matrix(v, h): # creating matix 2D of 1
    
    m = []    
    p = ['it\'s not a bug, it\'s a feature!!! So its going to be an message pop-up!, or not']
    
    for i in range (v + 1): 

        m.append(p)
        p = []   
        
        for j in range(h):

            p.append(1)
    
    return (m)

#OkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDoki

def start (coord):
    plane = copy.deepcopy(matrix( vertical, horizontal))
    
    for i in coord:
        
        plane[ int(i[0]) + 1][ int(i[1]) ] = 0
    
    print ('start \n')
    
    
    for i in range(len(plane) - 3): #prinitng starting point, making matrix more readable
        print (plane[i + 2][1:-1] )
    
    return (game_of_life(plane, vertical, horizontal, steps))

#OkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDokiOkiDoki


vertical = int(input('set number of columns\n')) + 2
horizontal = int(input('set number of rows\n')) + 2
steps = int(input('set number of cycles\n'))



l = []
l_check = []


# creating list containing coorigates of living cells
while 1 :
    a = str(input('h to print help\n'))
    
    if a == 's':
        break
    elif a =='h':
        
        print ('Type two integers separated by coma, e.g. \'4,5\'.\n '
               'To set living cell\n'
               "It\'s casesensitive! \n "
               "To set living cells at random type \'rand\',to start game type \'s\'.\n"
               "Be cautious while typing in, it's buggy")
        
        
    elif a == 'rand':
        
        c = int(input('set number of random cells\n'))
        
        
        while True:
            
            k = random.randint(1, vertical - 2) #to create set and list form the same numbers
            j = random.randint(1, horizontal - 2)
            
            cell = [k ,j]
            check = str(k) + ',' + str(j) #check is transformed into set, to get rid of duplicates
            
            
            l.append(cell)
            l_check.append(check)
            

            
            if len(set(l_check)) == c:
                print (l, "\nType 's' to start!\n")
                break
        
            
    else:
        b = a.split(',')
        l.append(b)
        print (l)

p = start (l)    


