# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:15:48 2022

@author: muham
"""


import random 
import copy
import math
class chromo:

    def __init__(self):
        self.gene = [None]*6
        for i in range(6):
            self.gene[i] = random.choice([0,1])
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
        a=x**2
        #print(a)
        b=(y-a)**2
        #print(b)
        c=(1-x)**2
        #print(c)
        d=c+100*(b)
        
        final_value =d
        self.fitness = final_value
solution = chromo()
# print(solution.gene)
# print(solution.fitness)

class operators:
    def truncation(pop, parent_count):
        new_population = sorted(pop, key = lambda x:x.fitness, reverse = True)
        # for i in range(len(pop)):
        #     print(new_population[i].fitness)
        return new_population[0], new_population[1]

    def mutate(child):
        print('mutation happening')
        print(child.gene, child.fitness)
        index = random.randint(0,len(child.gene)-1)
        print(index)
        child.gene[index] = random.choice([0,1])
        child.evaluate()
        print(child.gene, child.fitness)
        return child


    def one_point(parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        child1.gene[3:5] = parent2.gene[3:5]
        child2.gene[3:5] = parent1.gene[3:5]
        chromo.evaluate(child1)
        chromo.evaluate(child2)
        # print(child1.gene, child1.fitness, child2.gene, child2.fitness)
        return child1, child2


    def sur_random(pop):
        random.shuffle(pop)
        # for item in pop:
        #     print(item.gene, item.fitness)
        return pop[:10]


    def sur_truncation(pop):
        pop = sorted(pop, key = lambda x:x.fitness, reverse = True)
        # for item in pop:
        #     print(item.gene, item.fitness)
        return pop[:10]

    def BT_parent(pop, tour_size):
        tour_pop = []
        for i in range(tour_size):
            tour_pop.append(random.choice(pop))
        for item in tour_pop:
            print(item.fitness)
        tour_pop= sorted(tour_pop, key = lambda x:x.fitness, reverse = True)
        print(tour_pop[0].fitness)
        return tour_pop[0]