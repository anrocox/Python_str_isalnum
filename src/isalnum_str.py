#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

How to determine if a python str is alphanumeric?

¿Como determinar si un str python es alfanumerico?
'''

#create a str
s = 'abc123'
print(s)

#the isalnum() method verify if all characters in the str are alphanumeric.
#return True or False
print(s.isalnum())

#create a str
s = 'new string'
print(s)

#return False because it contains 'space' character
print(s.isalnum())

#return False because is a empty string
print(''.isalnum())
