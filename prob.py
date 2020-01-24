import random
random.random()
collection=[]


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
    

for i in range(1000):
    
    collection.append(onetime())

print(collection.count(True)/len(collection))



