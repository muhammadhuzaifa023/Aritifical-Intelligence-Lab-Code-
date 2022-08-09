# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:27:10 2022

@author: muham
"""

import random
import EA_Operators
pop_size=10
pop=[ _ for _ in range(pop_size)]
for i in range(10):
    pop[i]=EA_Operators.chromosome()
    print(pop[i].x,pop[i].y) # Chromosome class may say object initiate ker raha haii
    #print("x and y = fitnesss")
    print("x={},y={} and fitness={}".format(pop[i].x,pop[i].y,pop[i].fitness))
    #print(pop[i].x,pop[i].y,pop[i].fitness) #fitness x**2+y**2 
    #reuslt kuch es thara say araha haii 
    #(-5)^2+(0)^2=25 is fitness
    #-5 0 25  here (-5 is x ),(0 is y ) and 25 is fitness 
#parent1=EA_Operators.selection.rand_parent(pop)

#print(parent1.x,parent1.y,parent1.fitness)
#parent2=EA_Operators.selection.rand_parent(pop)
#print(parent2.x,parent2.y,parent2.fitness)
print("Selecting Best Patrent for the Generation ")
parent1,parent2=EA_Operators.selection.trunc(pop)
print("*******************")
print(parent1.x,parent1.y,parent1.fitness)
print("*******************")
print(parent2.x,parent2.y,parent2.fitness)
print("Making a children by cross over and check the fitness ")
child1,child2=EA_Operators.operator.one_point(parent1,parent2)
