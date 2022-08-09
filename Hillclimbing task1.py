# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:17:26 2022

@author: muham
"""
import random
import math
#f(x,y)=e-(x^2+y^2)
def generated_sol():
    rangeX = (-2, 2)
    rangeY = (-2, 2)
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    sol=x,y
    return sol
def Evaluate(sol):
    x,y=sol
    z=math.exp(-1*((x**2)+(y**2)))
    #value1 = -1 * (pow(x,2) + pow(y,2))
    #z = math.exp(value1)
    return z
def Generate_neighbours(sol):
    x,y=sol
    if random.random() > 0.5:
        if random.random() > 0.5:
            if x > 1.5:
                pass
            else:
                x += 0.5
        else:
            if x < -1.5:
                pass
            else:
                
                x -= 0.5
    else:
        if random.random() > 0.5:
            if y > 1.5:
                pass
            else:
                y += 0.5
        else:
            if y < -1.5:
                pass
            else:
                y -= 0.5
        
    
    return(x,y)
        
    
    
    
       
    #return(x,y)
sol=generated_sol()
score=Evaluate(sol)
print(sol)
print(Evaluate(sol))
print(Generate_neighbours(sol))
counter = 0
while True:
    # score = evaluate(guess_x,guess_y)
    # print("score is", score)
    counter += 1
    new_sol = list(sol)
    score = Evaluate(sol)
    print(counter, sol, score)
    if counter == 100:
        break
    
    new_sol = Generate_neighbours(new_sol)
    new_score = Evaluate(new_sol)
    
    if new_score>score:
        sol=new_sol
        score=new_score