# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:59:27 2015

@author: eafit
"""
from __future__ import division
import numpy as np
from sympy import init_printing
init_printing()
#
def readin():
#
# Reads the input files
#
    nodes    = np.loadtxt('nodes.txt')
    mats     = np.loadtxt('mater.txt')
    elements = np.loadtxt('eles.txt' )
    loads    = np.loadtxt('loads.txt')
#
    return nodes,mats,elements,loads
#
def proini(nodes,mats,elements,loads):
#
# Extracts problem parameters and
# nodal coordinates.
#
    ne =len(elements[:,0])
    nn =len(nodes[:,0])
    nm =len(mats[:])
    nl =len(loads[:,0])
    COORD  =np.zeros([nn,2],dtype=np.float)
    COORD[:,0]=nodes[:,1]
    COORD[:,1]=nodes[:,2]
#
    return ne,nn,nm,nl,COORD
#
def echomod(nodes,mats,elements,loads):
#
# Creates echos of the model input files.
#
    np.savetxt("KNODES.txt", nodes,    fmt='%5.2f', delimiter=' ')
    np.savetxt("KMATES.txt", mats,     fmt='%5.2f', delimiter=' ')
    np.savetxt("KELEMS.txt", elements, fmt='%5.2f', delimiter=' ')
    np.savetxt("KLOADS.txt", loads,    fmt='%5.2f', delimiter=' ')    
#
    return