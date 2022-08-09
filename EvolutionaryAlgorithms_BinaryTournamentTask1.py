# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:57:06 2022

@author: muham
"""

import copy
import EvolutionaryAlgorithms_Operators_BinaryTournamentTask1
import random

# initiate empty population
#import GA_Operators

pop = [_ for _ in range(10)]
#populate the initial population
for i in range(10):
    pop[i] = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.chromo(-2,2,-2,2)

for gen_count in range(100):
    
    print("GENERATION NO: ",gen_count)
    new_pop = []
      
    for i in range(5):
        parent1 = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.BT_parent(pop,2)
        parent2 = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.BT_parent(pop,2)
        # print('parent1',parent1.x,parent1.y,parent1.fitness)
        # print('parent2',parent2.x,parent2.y,parent2.fitness)
        child1, child2 = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.one_point(parent1,parent2)
        if random.random() < 0.1:
            if random.random() < .5:
                print('mutation')
                child1 = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.uniform_mutation(child1)
            else:
                child2 = EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.uniform_mutation(child2)
    
        #print('child',child1.x,child1.y,child1.fitness,child2.x,child2.y,child2.fitness)
        new_pop.append(child1)
        new_pop.append(child2)
        # print(new_pop)
        
        #EA_Operator.selection.trunc(pop)
        
    
    pop =EvolutionaryAlgorithms_Operators_BinaryTournamentTask1.operators.sur_truncation(pop + new_pop)
    for i in range(10):
        print(pop[i].x,pop[i].y,pop[i].fitness)    ## tgis remains


