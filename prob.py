import random
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





