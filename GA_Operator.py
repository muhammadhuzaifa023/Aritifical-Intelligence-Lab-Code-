# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:48:25 2022

@author: 19b-125-cs
"""
import copy
import random
class chromosome:
    def __init__(self):
        self.value=[None]*8
        for i in range(len(self.gene)):
            self.gene[i]=random.choice([0,1])
        self.evaluate()
    #Decoding functuion 
    def evaluate(self):
        value_x=self.gene[1]*4+self.gene[2]*2+self.gene[3]*1
        if self.gene[0]:
            value_x *=-1
        value_y=self.gene[5]*4+self.gene[6]*2+self.gene[7]*1
        if self.gene[4]:
            value_y *=-1
         
        print(value_x,value_y)
        value1=-1*(pow(value_x,2)+pow(value_y,2))
        value2=-1*(pow((value_x-1.7),2)+pow(value_y-1.7),2)
    def trunc_pop(pop):#top most parent select kerlayga
        sorted_pop=sorted(pop,key=lambda x:x.fitness,reverse=True)
        return sorted_pop[:10]
        
        
class selection:
    #randomly ek parent return kraygaa
    def rand_parent(pop):
        index=random.randint(0,len(pop)-1)
        indivi=copy.deepcopy(pop[index])
        #indivi=random.choice(pop)
        print(indivi)
        print("***",indivi.x,indivi.y,indivi.fitness)
        
        return(indivi)
class operator:
    def one_point(parent1,parent2):
        child1=copy.deepcopy(parent1)
        child2=copy.deepcopy(parent2)
        index=random.randint(0,len(parent1.gene))
        child1[index:]=parent2.gene[index:]
        child2[index:]=parent1.gene[index:]
        child1.evaluate()
        child2.evaluate()
        return child1,child2