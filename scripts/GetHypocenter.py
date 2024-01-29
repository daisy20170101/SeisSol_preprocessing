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
#import scipy.io as sio
import matplotlib.tri as tri
#from mpl_toolkits.basemap import Basemap

modelname = 'alkR057-TP54'
modelname = 't1'
foldername = '/import/deadlock-data/dli/Alaska2021/resultNew/'
foldername = 'result1938/'

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(init='EPSG:5936',ellps='WGS84', datum='WGS84')

xdmfFilename =foldername + modelname+'-fault.xdmf'

stall = np.loadtxt('hypo1938.dat')

staxyz= pyproj.transform(lla, myproj, stall[:,0],stall[:,1], stall[:,1], radians=False)

# find stations and read records
surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)-1

centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.
triang = tri.Triangulation(surfxyz[:,0]/1e3,surfxyz[:,1]/1e3,connect)

Receiver = np.array([staxyz[0],staxyz[1],staxyz[2]])
Receiver = Receiver.transpose()

#np.savetxt('hypo.xy',Receiver)

from scipy import spatial

tree = spatial.KDTree(centers)
dist, ids = tree.query(Receiver)
FidReceiversnew = 'hypo1938_xyz.txt'
fout = open(FidReceiversnew,'w')

for k in range(0,stall[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))

fout.close()

d1 = np.loadtxt('GMT/rupture1938.gmt',skiprows=1)

dd = np.loadtxt(FidReceiversnew)

fig,ax0=plt.subplots(nrows=1,ncols=1,figsize=(4,3.5))

ax0.plot(dd[:,0]/1e3,dd[:,1]/1e3,'*k',markersize=3)

sc = ax0.tripcolor(triang,centers[:,2]/1e3,cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax0)

plt.title('eastward  hypocenter')
plt.savefig('hypo1938.png',dpi=100)
    
