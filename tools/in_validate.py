#!/usr/bin/env python3
# Author: Raymond Chan
'''Functions for validating user input data
   get_digits(user_data) - return all digit characters from user input data
   get_chars(user_data,valid_chars) - return all valid characters from user input data
   get_chars2(user_data,valid_chars - return valid characters and invalides characters from user input data
   '''
def get_digits(obj):
    '''Take any string object and return all the
       digits 0-9 found as a string and keep their
       order in the string'''
    digits = ''
    for char in obj:
        if char in '0123456789':
            digits += char
    return digits
    
def get_chars(obj,chars):
    '''Take any string object and another string object which contains
       target characters to be extracted from the first sting object.
       Return all the target characters found in the first string 
       object as a string and keep their original order in the first 
       string.'''
    target = ''
    for char in obj:
        if char in chars:
            target += char
    return target
    
def get_chars2(obj,chars):
    '''Take any string object and another string object which contains
       target characters to be extracted from the first string object. 
       Return a two items tuple: (i) all the target characters found in the first 
       string object as a string and keep their original oreder in the first string,
       (ii) the rest of other characters in the first string object which are not
       in the target characters set.'''
    target = ''
    others = ''
    for char in obj:
        if char in chars:
            target += char
        else:
            others += char
    return target,others
