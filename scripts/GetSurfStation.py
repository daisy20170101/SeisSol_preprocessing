#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:36:25 2019

@author: root
"""

from pythonXdmfReader.pythonXdmfReader import *
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import scipy.io as sio
import matplotlib.tri as tri

modelname = 'alkR057-TP81b'
foldername = '/import/deadlock-data/dli/Alaska2021/resultNew/'
foldername = 'resultNew/'

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(init='EPSG:5936',ellps='WGS84', datum='WGS84')

xdmfFilename =foldername + modelname+'-surface.xdmf'

stall = np.loadtxt('gps_stations.dat')
staxyz= pyproj.transform(lla, myproj, stall[:,1],stall[:,0], stall[:,1], radians=False)

# find stations and read records
surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)-1

centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.
datapool = np.array(centers)
print(datapool.shape)

Receiver = np.array([staxyz[0],staxyz[1],staxyz[2]])
Receiver = Receiver.transpose()

rev = np.array([staxyz[0],staxyz[1]])
rev = rev.transpose()

from scipy import spatial

#tree = spatial.KDTree(centers)
tree = spatial.KDTree(datapool)

dist, ids = tree.query(Receiver)
FidReceiversnew = 'gps_mesh8.txt'
fout = open(FidReceiversnew,'w')

for k in range(0,stall[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=datapool[ids[k]]
        fout.write("%12.7e %12.7e %12.7e\n" %(newrec[0],newrec[1],newrec[2]))
        print(dist[k])

fout.close()


    
