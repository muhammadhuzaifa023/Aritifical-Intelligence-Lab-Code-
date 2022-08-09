# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:55:52 2022

@author: muham
"""

import copy
import random
import math
class chromo:
    def __init__(self,x1,x2,y1,y2):
        self.x = random.randint(x1,x2)
        self.y = random.randint(y1,y2)
        self.evaluate()

    def evaluate(self):
        self.fitness = math.exp(-1*(((self.x)**2)+((self.y)**2)))



class operators:

    def BT_parent(pop, tour_size):
        tour_pop = []
        for i in range(tour_size):
            tour_pop.append(random.choice(pop))
        for item in tour_pop:
            print(item.x, item.y, item.fitness)
        tour_pop= sorted(tour_pop, key = lambda x:x.fitness, reverse = True)
        print(tour_pop[0].fitness)
        return tour_pop[0]

    def one_point(parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        child1.y = parent2.y
        child2.y = parent1.y
        child1.evaluate()
        child2.evaluate()
        return child1, child2

    def uniform_mutation(child):
        if random.random() < .5:
            if random.random() < .5:
                child.x += .5
            else:
                child.x -= .5
        else:
            if random.random() < .5:
                child.y += .5
            else:
                child.y -= .5
        
        child.evaluate()
        return child

    def sur_truncation(pop):
        pop = sorted(pop, key = lambda x:x.fitness, reverse = True)
        # for item in pop:
        #     print(item.gene, item.fitness)
        return pop[:10]
