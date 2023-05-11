import pandas as pd
import matplotlib.pyplot as plt

#total number of initial single stars: 969, binaries: 322


              ### CHI METTE I PERCORSI ASSOLUTI DEVE MORIRE IN GALERA ###
sin0=pd.read_csv(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/M1000_D1.6_Z0.002/single.40_0'
                ,header=None, delim_whitespace=True,skiprows=1)
binn0=pd.read_csv(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/M1000_D1.6_Z0.002/binary.40_0'
                ,header=None, delim_whitespace=True,skiprows=1)

x0=sin0[2].values
y0=sin0[3].values
z0=sin0[4].values
xcm0=binn0[5].values
ycm0=binn0[6].values
zcm0=binn0[7].values


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x0,y0,z0,marker='.',color='b',s=10,label='single stars')
ax.scatter(xcm0,ycm0,zcm0,marker='.',color='r',s=10,label='binaries (CM)')
ax.set_xlabel('x(pc)')
ax.set_ylabel('y(pc)')
ax.set_zlabel('z(pc)')
plt.title('3d distribution at starting time, z=0.002')
plt.legend()
plt.show()

sin=pd.read_csv(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/M1000_D1.6_Z0.002/single.40_134'
                ,header=None, delim_whitespace=True,skiprows=1)
binn=pd.read_csv(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/M1000_D1.6_Z0.002/binary.40_134'
                ,header=None, delim_whitespace=True,skiprows=1)

x=sin[2].values
y=sin[3].values
z=sin[4].values
xcm=binn[5].values
ycm=binn[6].values
zcm=binn[7].values

plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z,marker='.',color='b',s=10,label='single stars')
ax.scatter(xcm, ycm, zcm,marker='.',color='r',s=10,label='binaries (CM)')
ax.set_xlabel('x(pc)')
ax.set_ylabel('y(pc)')
ax.set_zlabel('z(pc)')
plt.title('3d distribution at final time, z=0.002')
plt.legend()
plt.show()
