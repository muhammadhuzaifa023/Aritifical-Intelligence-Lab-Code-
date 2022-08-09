# -*- coding: utf-8 -*-
"""
Created on Wed May 25 08:59:01 2022

@author: 19b-125-cs
"""
# Evolution Algorithms 
import random
import EA_Operators
pop=[ _ for _ in range(10)]
for i in range(10):
    pop[i]=EA_Operators.chromosome()
    print(pop[i].x,pop[i].y,pop[i].fitness)
for gen_count in range(1000):
    print("generation",gen_count)
        
    new_pop=[]
    for i in range(5):# child ka loop hai pop size 10 tha jabhi 5 rakha 
    #5 dafa loop chalaygaa to ek loop ka chalnay say 2 child produce hooga 
    #5 * 2 =10 
    #parent1=EA_Operators.selection.rand_parent(pop)
    #print(parent1.x,parent1.y,parent1.fitness)
    #parent2=EA_Operators.selection.rand_parent(pop)
    #print(parent2.x,parent2.y,parent2.fitness)
        parent1,parent2=EA_Operators.selection.trunc(pop)
        child1,child2=EA_Operators.operator.one_point(parent1,parent2)# cross over step 4
        if random.random()<.5:#mutation in child  step 5 mutation in child 
            print("mutatiuon happing")
            if random.random()<.5:
                print("Mutation in child 1")
                child1=EA_Operators.operator.uniform_mutation(child1)
            else:
                print("Mutation in child 2")
                child2=EA_Operators.operator.uniform_mutation(child2)
        print(child1.x,child1.y,child1.fitness,child2.x,child2.y,child2.fitness)
        new_pop.append(child1)
        new_pop.append(child2)
        
    pop=EA_Operators.selection.trunc_pop(pop+new_pop)
    print(pop)# prevoius popultaion and new population 10 +10 =20
    print("-------------------------------------")
    print(new_pop)
    for i in range(10): # PICKING THE BEST 10 FROM 20 
        
        print(pop[i].x,pop[i].y,pop[i].fitness)

#new_pop
    