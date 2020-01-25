import random
# import numpy as np
from matplotlib import pyplot
random.random()

collectionA50=[]
collectionA100=[]
collectionA1000=[]
collectionA10000=[]
collectionA=[]

collectionB50=[]
collectionB100=[]
collectionB1000=[]
collectionB10000=[]
collectionB=[]

collectionC50=[]
collectionC100=[]
collectionC1000=[]
collectionC10000=[]
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
    

for i in range(50):
    
    collectionA50.append(onetime())
    collectionB50.append(twotime())
    collectionC50.append(threetime())


for i in range(100):
    
    collectionA100.append(onetime())
    collectionB100.append(twotime())
    collectionC100.append(threetime())

for i in range(1000):
    
    collectionA1000.append(onetime())
    collectionB1000.append(twotime())
    collectionC1000.append(threetime())

for i in range(10000):
    
    collectionA10000.append(onetime())
    collectionB10000.append(twotime())
    collectionC10000.append(threetime())


for i in range(100000):
    
    collectionA.append(onetime())
    collectionB.append(twotime())
    collectionC.append(threetime())







print(collectionA.count(True)/len(collectionA))
print(collectionB.count(True)/len(collectionB))
print(collectionC.count(True)/len(collectionC))






x= [50,100,1000,10000,100000]

y= [collectionA50.count(True)/50,
    collectionA100.count(True)/100,
    collectionA1000.count(True)/1000,
    collectionA10000.count(True)/10000,
    collectionA.count(True)/100000
    ]



pyplot.scatter(x, y, label="1st experimental")

pyplot.title('Probability')
pyplot.xlabel('Number of Try')
pyplot.ylabel('Probability')


pyplot.show()





