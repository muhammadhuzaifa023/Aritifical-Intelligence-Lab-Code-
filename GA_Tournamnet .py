# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:43:30 2022

@author: muham
"""



import GA_OperatorTournament
import random
print("f(x,y)=e^-(x**2+y**2)")
# initiate empty population
pop = [_ for _ in range(10)]
#populate the initial population
for i in range(10):
    pop[i] = GA_OperatorTournament.chromo()

# for i in range(10):
#     print(pop[i].gene, pop[i].fitness)


print(pop)
for p in range(100):
    new_pop = []
    for i in range(5):
        parent1 = GA_OperatorTournament.operators.BT_parent(pop, 2)
        parent2 =GA_OperatorTournament.operators.BT_parent(pop, 2)
        print(parent1.gene, parent1.fitness)
        print(parent2.gene, parent2.fitness)
        child1, child2 =GA_OperatorTournament.operators.one_point(parent1, parent2)
        number = random.random()
        if number <  .001:
            if random.random() < .5:
                child1 = GA_OperatorTournament.operators.mutate(child1)
            else:
                child2 = GA_OperatorTournament.operators.mutate(child2)
        new_pop.append(child1)
        new_pop.append(child2)

    # for i in range(10):
    #     print(new_pop[i].gene, new_pop[i].fitness)
    print('************************************ generation count', p)
    pop = GA_OperatorTournament.operators.sur_truncation(pop+new_pop)

    for item in pop:
        print(item.gene, item.fitness)
