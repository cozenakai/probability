import random
random.random
game=[]

def onetime():
    list=[]
    
    for i in range(2):
        bat = random.randint(1, 10)
        list.append(bat)

    if list==[1,1]:
        return True
    else:
        return False


for i in range(100000):
    game.append(onetime())


print(game.count(True)/len(game))
    