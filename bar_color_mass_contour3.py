import scipy.ndimage     #for smooth contour
from scipy.ndimage.filters import gaussian_filter  # for smooth contour
from scipy.stats import binned_statistic
from scipy import stats
from scipy import interpolate 
import numpy as np           # to define our table
from scipy.interpolate import griddata
import statistics
import matplotlib.mlab
import matplotlib.tri as tri
import matplotlib
import matplotlib.pyplot as p
import sys


BG_li=[] # barred galaxies
NBG_li=[] # unbarred galaxies
colorB_li=[]
colorNB_li=[]
logMB_li=[]
logMNB_li=[]

d='bar_color_mass.dat'              
data=np.loadtxt(d,dtype={'names':('WINGS','Bar','Color','logM2'),'formats': ('O','f','f','f')} ,skiprows=1)

WINGS=data['WINGS']
Bar=data['Bar']     ## contours
color=data['Color']  ## y-axis   
logM =data['logM2']  ## x-axis


for i in range(len(Bar)):
    if Bar[i]==0:
       NBG=Bar[i]
       colorNB=color[i]
       logMNB=logM[i]
       NBG_li.append(NBG)
       colorNB_li.append(colorNB)
       logMNB_li.append(logMNB)
    else:
        BG=Bar[i]
        colorB=color[i]
        logMB=logM[i]
        BG_li.append(BG)
        colorB_li.append(colorB)
        logMB_li.append(logMB)
        
print('barred',len(BG_li))
print('unbarred',len(NBG_li))
 



binx=np.linspace(8.3,11.7,7)  
print('binx',binx)

biny=np.linspace(0.2,1.4,7)  
print('biny',biny)


xi=binx
yi=biny
zi = griddata((logM, color), Bar, (xi[None,:], yi[:,None]), method='cubic')

#p.contour(xi, yi, zi)
#p.show()


###This function supports both indexing conventions through the indexing keyword argument. Giving the string ‘ij’ returns a meshgrid with matrix indexing, while ‘xy’ returns a meshgrid with Cartesian indexing. In the 2-D case with inputs of length M and N, the outputs are of shape (N, M) for ‘xy’ indexing and (M, N) for ‘ij’ indexing.####

#xgrid,ygrid = np.meshgrid(binx, biny)
#print('xgrids',xgrid, len(xgrid))
#print('ygrids',ygrid, len(ygrid))


#p.plot(xgrid, ygrid,marker='.', color='k', linestyle='none')
#p.show()



#for i in range(len(xgrid)):
   # for j in range(len(ygrid)):






#print('x_li_shape',x_li.shape)

#zi =griddata((x_array, y_array), z_array, (xi[None,:], yi[:,None]), method='cubic')
#print('zi',zi)

#Xi, Yi = np.meshgrid(xi, yi)
#zi = interpolate.interp1d(xi, yi)

#sys.exit()



#Z=[]

## Linearly interpolate the data (x, y) on a grid defined by (xi, yi).
#triang = tri.Triangulation(x_li, y_li)
#interpolator = tri.LinearTriInterpolator(triang, z_li)
#Xi, Yi = np.meshgrid(xi, yi)
#zi = interpolator(Xi, Yi)


p.figure(1)



#CS = plt.contour(xi,yi,zi,15,linewidths=0.5,colors='k')
#CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
p.scatter([logMNB_li],[colorNB_li],s=10,  marker='^', color='grey',label='Unbarred')
p.scatter([logMB_li],[colorB_li], s=14, marker='+', color='black', alpha=0.5, label='Barred')
CS=p.contour(xi,yi,zi,[0.1,0.2,0.3,0.4,0.5])
#p.clabel(CS, inline=1, fontsize=10)
labels = ['fbar=0.1', 'fbar=0.2','fbar=0.3','fbar=0.4','fbar=0.5']
for i in range(len(labels)):
    CS.collections[i].set_label(labels[i])
p.legend(loc='upper left')
p.xlabel ('logM', fontsize=20)
p.ylabel ('(B-V)', fontsize=20)
p.xlim(8.5,11.7)
p.ylim(0.2,1.4)
p.legend(fontsize=10, loc='lower right')
#p.text(-3.5, 0.5, r'(b)', fontsize=20) ## to insert a label inside the plot
p.subplots_adjust(left=0.2, bottom=0.2, top=0.85)
p.savefig('Bar_color_mass_trial3.png')
p.close()




