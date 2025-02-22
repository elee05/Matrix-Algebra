import matplotlib.pyplot as plt
import numpy as np
import random
import math

colors = ["r","b","g","c","m","y","k"]

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 3, 5])

def plotVectorSet(x,y):
    fig, ax = plt.subplots()
    ax.set_xlim(-max(x),max(x))
    ax.set_ylim(-max(y),max(y))
    for i in range(len(x)):
        ax.quiver(0,0,x[i],y[i], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))
    plt.show()

def plotVectorAddition(v1,v2):
    fig, ax = plt.subplots()
    r = v1+v2
    ax.set_xlim(-1.5*r[0],1.5*r[0])
    ax.set_ylim(-1.5*r[1],1.5*r[1])

    ax.quiver(0,0,v1[0],v1[1], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))
    ax.quiver(0,0,v2[0],v2[1], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))
    ax.quiver(0,0,r[0],r[1], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))

    ax.quiver(v1[0],v1[1],v2[0],v2[1], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))
    ax.quiver(v2[0],v2[1],v1[0],v1[1], angles = "xy", scale_units = "xy", scale = 1, color = random.choice(colors))
    
    plt.show(block=False)

    nen = input("press enter when done: ")
    plt.close()


def main():
    while True:
        print("vector addition visualization")
        v1 = np.zeros([2])
        v2 = np.zeros([2])
        v1[0] = input("type x component of first vector: ")
        #if (v1 == "exit"):
         #   break
        print()
        v1[1] = input("type y component of first vector: ")
        print()
        v2[0] = input("type x component of second vector: ")
        print()
        v2[1] = input("type y component of second vector: ")
        print()
        
        plotVectorAddition(v1,v2)
        con = input("press enter to continue or type 'exit' to end: ")
        if (con == "exit"):
            break
        

main()
#v1 = np.array([1,5])
#v2 = np.array([5,1])
#plotVectorAddition(v1,v2)
#plotVectorSet(x,y)