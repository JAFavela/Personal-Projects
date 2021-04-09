# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:19:40 2020

@author: jorge
"""


import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
L=os.environ['PATH'].split(';')
p = os.getcwd() + '\\geko'

if(p not in L):
    os.environ['PATH'] = os.environ['PATH']+';'+p
    
# os.system(os.getcwd()+'\\GoldMiner_v0.2.exe')
# os.system('python '+ os.getcwd()+'\\browser.py')
os.system('python '+ os.getcwd()+'\\main.py')
# os.system(os.getcwd()+'\\main.exe')
