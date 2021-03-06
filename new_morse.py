#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:14:21 2020

@author: szatko
"""

MORSE_CODE = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

#morse code - words separated by 4x' ', leters by ' '

def encoding(string):
    
    coded = ''
    string = string.upper() #case sensitive

    for i in range(len(string)):
       if string[i] == ' ':
          coded += '   '
       else:
           coded += MORSE_CODE[string[i]] + ' '
    return coded.strip()
    


def decoding(code):
    #spliting into words
    code = code.strip().split('    ')
    
    words = []
    msg = ''
    
    keys = list(MORSE_CODE.keys())
    values = list(MORSE_CODE.values())
    
    for word in code:
        #spliting into letters
        word = word.split()
        x = ''
        
        for letter in word:
            #interpreting letters
            index = values.index(letter)
            x += keys[index]
        
        words.append(x)
    #creating decoded message
    for i in words:
        msg += i +  ' '
        
    return msg.strip()
  
