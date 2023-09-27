#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/20/2023
#This program implement the piece of pseudocode as a complete program.

import numpy as np
from matplotlib import pyplot as plt

num = int(input("Enter the size: "))
output = input("Enter output file: ")

# num = 50
# output = "stripes50.png"

graph = np.ones([num,num,3])

for i in range(num):
    if i%2==0:
        graph[::1,:,0:3]=1.0
        graph[::1,:,2]=0

    else:
        graph[::2,:,0:3]=1.0
        graph[::2,:,1]=0
        # graph[::2,:,2:]=1.0
    #     graph[::1,:,2]=0

plt.imsave(output,graph)