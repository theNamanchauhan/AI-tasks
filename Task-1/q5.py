# QUESTION 5

import csv
import numpy as np
import matplotlib.pyplot as plt
f=open("q5.csv","w")
cwriter=csv.writer(f)
x=[]
y=[]
l=[]
for i in range(700,2401):
    if i%10==0:
        x.append(i)
        
for i in x:
    eq=10*i^2+2*i
    y.append(eq)
    
for i in range(len(x)):
    l1=[x[i],y[i]]
    l.append(l1)

cwriter.writerows(l)

f.close()
a = []
b = []
  
with open('q5.csv','r',newline='\r\n') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        a.append(row[0])
        b.append(row[1])
        
data = np.genfromtxt("q5.csv", delimiter=",", names=["x", "y"])
plt.plot(data['x'], data['y'])
plt.xlabel('Size(sq.feets)')
plt.ylabel('Price')

