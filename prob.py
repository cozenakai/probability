import random
# import numpy as np
from matplotlib import pyplot
random.random()

theory1= 55/216
theory2=(3+10+21+27+25+15+6+1)/216
theory3=25/216

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






x= ['50','100','1000','10000','100000']

y= [collectionA50.count(True)/50,
    collectionA100.count(True)/100,
    collectionA1000.count(True)/1000,
    collectionA10000.count(True)/10000,
    collectionA.count(True)/100000
    ]
y2= [theory1,theory1,theory1,theory1,theory1]

y3=[collectionB50.count(True)/50,
    collectionB100.count(True)/100,
    collectionB1000.count(True)/1000,
    collectionB10000.count(True)/10000,
    collectionB.count(True)/100000]

y4=[theory2,theory2,theory2,theory2,theory2]

y5=[collectionC50.count(True)/50,
    collectionC100.count(True)/100,
    collectionC1000.count(True)/1000,
    collectionC10000.count(True)/10000,
    collectionC.count(True)/100000]

y6=[theory3,theory3,theory3,theory3,theory3]

pyplot.plot(x,y)

pyplot.plot(x,y2)

pyplot.title('Problem1')
pyplot.xlabel('Number of Try')
pyplot.ylabel('Probability')


pyplot.show()

pyplot.plot(x,y3)

pyplot.plot(x,y4)

pyplot.title('Problem2')
pyplot.xlabel('Number of Try')
pyplot.ylabel('Probability')


pyplot.show()#忘れない

pyplot.plot(x,y5)

pyplot.plot(x,y6)

pyplot.title('Problem3')
pyplot.xlabel('Number of Try')
pyplot.ylabel('Probability')


pyplot.show()#忘れない









