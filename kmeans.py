!head StoneFlakes.dat
import pandas
import numpy as np
d = pandas.read_csv(open('StoneFlakes.dat'))
d = pandas.read_csv(open('StoneFlakes.dat'),sep=',')
! tr -s ' ' ',' < StoneFlakes.dat > StoneFlakes2.dat
! head StoneFlakes2.dat

import matplotlib.pyplot as plt
from copy import *
%matplotlib inline

data1 = d.iloc[:,1:].values
data = deepcopy(data1)
data.shape

plt.plot(data1);
plt.savefig("sf.png")

def calcJ(data,centers):
    diffsq = (centers[:,np.newaxis,:] - data)**2
    return np.sum(np.min(np.sum(diffsq,axis=2), axis=0))
ef kmeans(data, k = 2, n = 5):
    # Initialize centers and list J to track performance metric
    centers = data[np.random.choice(range(data.shape[0]),k,replace=False),:]
    J = []
    
    # Repeat n times
    for iteration in range(n):
                
        # Which center is each sample closest to?
        sqdistances = np.sum((centers[:,np.newaxis,:] - data)**2, axis=2)
        closest = np.argmin(sqdistances, axis=0)
        
        # Calculate J and append to list J
        J.append(calcJ(data,centers))
        
        # Update cluster centers
        for i in range(k):
            centers[i,:] = data[closest==i,:].mean(axis=0)
            
    # Calculate J one final time and return results
    J.append(calcJ(data,centers))
    return centers,J,closest
    
centers,J,closest = kmeans(data,2,5)
plt.plot(J);
plt.savefig("sfji.png")


kVal = []
jVal = []
for k in range(20):
        a,j,c= kmeans(data1,(k+2),300)
        j=j[-1]
        jVal.append(j)
        kVal.append(k+2)
plt.plot(kVal,jVal)
plt.savefig("sfjk.png")
