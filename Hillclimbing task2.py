# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:54:07 2022

@author: muham
"""


import random
import math
#f(x,y)=e-(x^2+y^2)
def generated_sol():
    rangeX = (-2.0, 2.0)
    rangeY = (-1.0, 3.0)
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    sol=x,y
    return sol
def Evaluate_Score(sol):
    x,y=sol
    #print(x,y)
    a=x**2
    #print(a)
    b=(y-a)**2
    #print(b)
    c=(1-x)**2
    #print(c)
    d=c+100*(b)
    return(d)
    
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
            if y > 2.5:
                pass
            else:
                y += 0.5
        else:
            if y < 2.5:
                pass
            else:
                y -= 0.5
        
    
    return(x,y)
        
sol=generated_sol()
score=Evaluate_Score(sol)
print(sol)
print(Evaluate_Score(sol))
print(Generate_neighbours(sol))
counter = 0
while True:
    # score = evaluate(guess_x,guess_y)
    # print("score is", score)
    counter += 1
    new_sol = list(sol)
    score = Evaluate_Score(sol)
    print(counter, sol, score)
    if counter == 100:
        break
    
    new_sol = Generate_neighbours(new_sol)
    new_score = Evaluate_Score(new_sol)
    
    if new_score>score:
        sol=new_sol
        score=new_score