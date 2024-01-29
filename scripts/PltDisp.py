#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:54:07 2021

@author: duoli
"""
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import matplotlib.tri as tri
import scipy.io as sio
from pythonXdmfReader.pythonXdmfReader import *


folder ='result1/'
modelname ='tp19'

lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
myproj = pyproj.Proj(proj='geocent',init='EPSG:5936',ellps='WGS84', datum='WGS84')
# myproj = pyproj.Proj(proj='utm',zone='5N',ellps='WGS84', datum='WGS84')

xdmfFilename = folder + modelname+'-surface.xdmf'
surf = ReadGeometry(xdmfFilename)
connect = ReadConnect(xdmfFilename)
ndt = ReadNdt(xdmfFilename)

#%%
flonlat =  pyproj.transform(myproj,lla,surf[:,0],surf[:,1],radians=False)
triang2 = tri.Triangulation(flonlat[0],flonlat[1],connect)
# triang = tri.Triangulation(surf[:,0]/1000,surf[:,1]/1000,connect)

slpz = LoadData(xdmfFilename,'W',connect.shape[0],idt=ndt-1,oneDtMem=True,firstElement=-1)

coastf = './coastline/alaska.mat'
coast = sio.loadmat(coastf)

fin = open( './surface_deformation.disp','r')
sdisp = np.loadtxt(fin,comments='#',skiprows=1)

#%%
# fig,([ax2,ax3])=plt.subplots(ncols=2,nrows=1,figsize=(9,6))
plt.figure(figsize=(9,3))

ax2=plt.subplot(121)
sc1=ax2.scatter(sdisp[:,0]-360, sdisp[:,1],s=80,c=sdisp[:,5],cmap='seismic',vmin=-3.0,vmax=3.0)
ax2.set(xlim=(-162, -154),ylim=(52, 59))
# ax2.set_ylabel('E component')
ax2.set_title('Inversion(USGS)')
ax2.plot(coast['data'][:,0],coast['data'][:,1],'-k',linewidth=0.5)
cl = plt.colorbar(sc1,ax=ax2)

ax3=plt.subplot(122)
sc2 = ax3.tripcolor(triang2,slpz[0],cmap='seismic',shading='flat',vmin=-3.0,vmax=3.0)
ax3.set(xlim=(-162,-154),ylim=(52,59))
ax3.plot(coast['data'][:,0],coast['data'][:,1],'-k',linewidth=0.5)
ax3.set_title('Simulation')
cl= plt.colorbar(sc2,ax=ax3)
cl.set_label('vertical displacement (m)')

# ax2=plt.subplot(323)
# ax2.scatter(surfxyz[0]/1e3,surfxyz[1]/1e3,c=sdisp[:,4],cmap='seismic',vmin=-1.0,vmax=1.0)
# ax2.set(xlim=(1.e3, 1.8e3),ylim=(-2.4e3,-1.4e3))
# ax2.set_ylabel('N component')
# ax2.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)

# ax3=plt.subplot(324)
# sc = ax3.tripcolor(triang,slpy[0],cmap='seismic',shading='flat',vmin=-1.0,vmax=1.0)
# ax3.set(xlim=(1.e3, 1.8e3),ylim=(-2.4e3,-1.4e3))
# ax3.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)

# ax2=plt.subplot(325)
# ax2.scatter(surfxyz[0]/1e3,surfxyz[1]/1e3,c=sdisp[:,5],cmap='seismic',vmin=-1.0,vmax=1.0)
# ax2.set(xlim=(1.e3, 1.8e3),ylim=(-2.4e3,-1.4e3))
# ax2.set_ylabel('U component')
# ax2.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)

# ax3=plt.subplot(326)
# sc = ax3.tripcolor(triang,slpz[0],cmap='seismic',shading='flat',vmin=-1.0,vmax=1.0)
# ax3.set(xlim=(1.e3, 1.8e3),ylim=(-2.4e3,-1.4e3))
# ax3.plot(ncst[0]/1e3,ncst[1]/1e3,'-k',linewidth=0.5)


plt.show()


outname = './'+ modelname +'-surfxyz.png'
plt.savefig(outname,dpi=150,transparent=False)
