# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:03:06 2022

@author: muham
"""

import random 
import copy
import math
import numpy as np
class chromo:

    def __init__(self):
        self.gene = [None]*6
        for i in range(6):
            self.gene[i] = random.choice([0,1])
            self.gene[i]=np.invert(self.gene[i],out=None)
            #if self.gene[i][1:3]==[1,1] or self.gene[i][4:6]==[1,1]:
            #self.gene[i]==[0,1,1,1,1,1] or self.gene[i]==[1,1,1,1,1,1] or self.gene[i]==[1,0,1,1,1,1] or self.gene[i]==[1,1,1,1,0,1]:
            
            #self.gene[i]== random.choice([0,1])
        self.evaluate()

     
    def evaluate(self):
        x = (2*self.gene[1] + 1*self.gene[2])
        if self.gene[0] == 1:
            x = x*-1
        y = ( 2*self.gene[4] + 1*self.gene[5])
        if self.gene[3] == 1:
            y = y*-1
        #value1 = -1* (pow(x,2) + pow(y,2))
        #value2 = -1 * (pow((x-1.7),2)+pow((y-1.7),2))
        final_value =math.exp(-1*((x**2)+(y**2)))
        self.fitness = final_value
solution = chromo()
print(solution.evaluate())
pop = [_ for _ in range(10)]
#populate the initial population
for i in range(10):
    pop[i] = chromo()

# for i in range(10):
    print(pop[i].gene, pop[i].fitness)