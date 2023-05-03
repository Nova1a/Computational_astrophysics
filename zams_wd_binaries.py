import pandas as pd
import matplotlib.pyplot as plt
import glob
import re

#name=i[55:59]

#select the final binary.40 for every cluster
all_dir=glob.glob(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/*')
maxtime=[]
for i in all_dir:
    all_files=glob.glob(i+r'/binary.40_*')
    m=max(all_files, key=lambda all_files:int(re.split('binary.40_',all_files)[1]))
    maxtime.append(m)

#extract masses, id and star type at final time (binary.40_maxtime)
#add to the dataframe the total mass of the clusters
datafin=[]
for f in maxtime:
    bin_fin=pd.read_csv(f,header=None, delim_whitespace=True,skiprows=1, 
                        usecols=[0,1,3,4,32,33])  
    name=f[55:59]
    bin_fin['masstot']=name
    datafin.append(bin_fin)
datfin=pd.concat(datafin, axis=0)
datfin.columns=['id1','id2','mass1','mass2','type1','type2','masstot']


#extract masses, id and star type at initial time (binary.40_0)
#add to the dataframe the total mass of the clusters
datain=[]
allf=glob.glob(r'/Users/irmaberveglieri/Desktop/data/D1.6_Z0 copia.002/*/binary.40_0')
for f in allf:
    bin_in=pd.read_csv(f,header=None, delim_whitespace=True,skiprows=1,
                       usecols=[0,1,3,4,32,33])
    name=f[55:59]
    bin_in['masstot']=name
    datain.append(bin_in)
datin=pd.concat(datain, axis=0)
datin.columns=['id1','id2','mass1','mass2','type1','type2','masstot']

#separate every binary system to have a list of single stars (maxtime)
#now i have a dataframe with mass, id, type of every star, and total mass of cluster
melt_ids_fin=datfin.melt(id_vars=['masstot'],value_vars=['id1','id2'],value_name='ids',
               var_name='1or2')
melt_masses_fin=datfin.melt(id_vars=['masstot'],value_vars=['mass1','mass2'],
                value_name='mass', var_name='m1or2')
melt_types_fin=datfin.melt(id_vars=['masstot'],value_vars=['type1','type2'],
                value_name='types', var_name='t1or2')
allfin=pd.concat([melt_ids_fin,melt_masses_fin,melt_types_fin],axis=1)
allfin=(allfin.drop(['1or2','m1or2','t1or2'],axis=1)).T.drop_duplicates().T

#select only the stars that are white dwarfs based on their type
#from the maxtime dataframe
wdtype=[10,11,12]  #white dwarfs types
wd=allfin[allfin.types.isin(wdtype)]

#same for the initial time
#dataframe with mass, id, type of every star, and total mass of cluster
melt_ids_in=datin.melt(id_vars=['masstot'],value_vars=['id1','id2'],value_name='ids',
               var_name='1or2')
melt_masses_in=datin.melt(id_vars=['masstot'],value_vars=['mass1','mass2'],
                value_name='mass', var_name='m1or2')
melt_types_in=datin.melt(id_vars=['masstot'],value_vars=['type1','type2'],
                value_name='types', var_name='t1or2')
allin=pd.concat([melt_ids_in,melt_masses_in,melt_types_in],axis=1)
allin=(allin.drop(['1or2','m1or2','t1or2'],axis=1)).T.drop_duplicates().T

#select from the initial time the stars with same id as in wd
zams=allin[allin.set_index(['masstot','ids']).index.isin(wd.set_index(['masstot','ids']).index)]

#take zams mass of star at initial time
#and corresponding mass of wd from final time
mzams=zams.mass.tolist()
mwd=wd.mass.tolist()
plt.scatter(mzams,mwd)
plt.xlabel('M_zams')
plt.ylabel('M_wd')
plt.show()





    


    
    
