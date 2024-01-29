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
from mpl_toolkits.basemap import Basemap

modelname = 'alkR057-TP64p'
foldername = '/import/deadlock-data/dli/Alaska2021/resultNew/'

xdmfFilename =foldername + modelname+'-fault.xdmf'

# find stations and read records
surfxyz = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)-1
centers = (surfxyz[connect[:,0]] + surfxyz[connect[:,1]] + surfxyz[connect[:,2]])/3.
triang = tri.Triangulation(surfxyz[:,0]/1e3,surfxyz[:,1]/1e3,connect)


#lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
#myproj = pyproj.Proj(init='EPSG:5936',ellps='WGS84', datum='WGS84')
#
#stall=np.array([[-158,-157.5,-157,-156.5,-156],[55.2,55.3,55.4,55.5,55.6]])
#stall = stall.transpose()
#print(stall.shape)
#staxyz= pyproj.transform(lla, myproj, stall[:,0],stall[:,1], stall[:,1], radians=False)

#%%
staxyz=np.array([[1456233.85,-1924749.19,-28e3],[1506233.85,-1894749.19,-28e3],[1556233.85,-1864749.19,-28e3],[1556233.85,-1884749.19,-25e3],[1556233.85,-1904749.19,-25e3]])


Receiver = np.array([staxyz[:,0],staxyz[:,1],staxyz[:,2]])
Receiver = Receiver.transpose()

from scipy import spatial

tree = spatial.KDTree(centers)
dist, ids = tree.query(Receiver)
FidReceiversnew = 'faultreceiver1.txt'
fout = open(FidReceiversnew,'w')

for k in range(0,staxyz[:,0].size):
        #newrec = find_nearest_vector(centers, rec)
        newrec=centers[ids[k]]
        fout.write("%f %f %f\n" %(newrec[0],newrec[1],newrec[2]))

fout.close()

#%%
dd = np.loadtxt('faultreceiver1.txt')
fig,([ax0,ax1])=plt.subplots(nrows=1,ncols=2,figsize=(9,3.5))

ax0.plot(dd[:,0]/1e3,dd[:,1]/1e3,'*w',markersize=3)
ax0.set(xlim=(1.2e3, 1.75e3),ylim=(-2.2e3,-1.6e3))

sc = ax0.tripcolor(triang,centers[:,2]/1e3,cmap='plasma',shading='flat')
cl = fig.colorbar(sc,ax=ax0)

plt.title('fault receivers')
plt.savefig('faultreceiver1.png',dpi=100)

    
