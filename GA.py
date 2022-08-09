# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:48:06 2022

@author: 19b-125-cs
"""

import GA_Operator
pop_size=10
pop=[ _ for _ in range(pop_size)]
for i in range(10):
    pop[i]=GA_Operator.chromosome()
    print(pop[i].x,pop[i].y)
for i in range(5):
    parent1=GA_Operator.selection.rand_parent(pop)
    parent2=GA_Operator.selection.rand_parent(pop)
    print(parent1.gene,parent1.fitness)
    
    
