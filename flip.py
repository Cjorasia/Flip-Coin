import random

list=[]

x=int(input("Enter number of samples: "))

choose=input("Enter heads or tails [heads/tails]")

heads=0
tails=0

# taking random inputs
for i in range(x):

    flip =random.randint(0,1)

    if flip == 1 :
        list.append(1)
        heads=heads+1
    else:
        list.append(0)
        tails=tails+1

# heads or tails... who wins!
if heads>tails:
    win=heads
else:
    win=tails

# win or loose
if choose == win:
    print("congrats! you win")
else:
    print("you loose! better luck next time")

res = input("wants to see samples taken!!! [y/n]")

# taken samples
if res=="y":
    print(list)
else:
    exit
