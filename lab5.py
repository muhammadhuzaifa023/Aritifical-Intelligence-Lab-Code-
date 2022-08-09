# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
 # -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:31:18 2022

@author: 19b-125-cs
"""


import random
import string

#this is our peak
guess='this !!'

sol=[]
    
#for i in range(len(guess)):
 #   sol.append(random.choice(string.printable))
#print(sol)
def generate_solution(len_guess):
    return([random.choice(string.printable) for _ in range(len_guess)])
sol=generate_solution(len(guess))

 
def evaluate(sol,guess):
    fitness=0
    for i in range(len(guess)):
        fitness+=abs(ord(sol[i])-ord(guess[i]))
    return fitness

def gen_neighbor(sol):
    index=random.randint(0,len(sol)-1)
    sol[index]=random.choice(string.printable)
    return sol

#print(sol)
score=(evaluate(sol,guess))
#print(gen_neighbor(sol))
#print(evaluate(sol,guess))
counter=0
while True:
    counter+=1
    print(counter,sol,score)
    new_sol=list(sol)
    score=evaluate(new_sol,guess)
    
    if score==0:
        break
    
    new_sol=gen_neighbor(new_sol)
    new_score=evaluate(new_sol,guess)
    print(sol,new_score)
    if score>new_score:
        sol=new_sol
        score=new_score


   
    
    
    
    
    