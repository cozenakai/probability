import random
import numpy as np
from matplotlib import pyplot
random.random()
collectionA=[]
collectionB=[]
collectionC=[]


def onetime():
    list=[]
    
    for i in range(3):
        saikoro = random.randint(1, 6)
        list.append(saikoro)
    sum=(list[0]+list[1]+list[2])
    if sum > 12 and sum < 18:
        return True
    else:
        return False

def twotime(): 
    list=[]
    
    for i in range(3):
        saikoro = random.randint(1, 6)
        list.append(saikoro)
    sum=(list[0]+list[1]+list[2])  
    if sum%2==0:
        return True
    else:
        return False
def threetime():
    list=[]
    
    for i in range(3):
        saikoro = random.randint(1, 6)
        list.append(saikoro)
    sum=(list[0]+list[1]+list[2])
    if sum/3==4:
        return True
    else:
        return False        
    

for i in range(100000):
    
    collectionA.append(onetime())
    collectionB.append(twotime())
    collectionC.append(threetime())

print(collectionA.count(True)/len(collectionA))
print(collectionB.count(True)/len(collectionB))
print(collectionC.count(True)/len(collectionC))




x= np.linspace(50,1000000,10)
y= 55/216



pyplot.plot(x, y, label="1st theooretical")

pyplot.title('Probability')
pyplot.xlabel('Number of Try')
pyplot.ylabel('Probability')

plt.legend()
pyplot.show()





