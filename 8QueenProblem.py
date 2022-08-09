# -*- coding: utf-8 -*-

#Hill Climbing Problem
#First Choice hill Climbing 
#+variation of Random 
import random

def generated_sol():
    sol=[(random.randint(0,7)) for _ in range(8)]
    return sol
   
def evaluate(sol):
    count=0
    # row ki space ko khatam ker rahay haii 
    for i in range(len(sol)):
        for j in range(len(sol)):
            if i ==j:
                continue
            if sol[i]==sol[j]:
                count+=1
            # diagonal khtam ker rahy haii                
            if abs(i-j)==abs(sol[i]-sol[j]):
                count+=1
    return(count)
def generate_neighbour(sol):
    index=random.randint(0,len(sol)-1)
    sol[index]=random.randint(0,7)
    return(sol)

#If I will styuck on Local Minimam so  what will I sdoo
sol=generated_sol()
print(sol)
score=evaluate(sol)
count=0
while True:
    count+=1
    print(count,sol,score)
    new_sol=list(sol)
    if score==0:
        break
    new_sol=generate_neighbour(new_sol)
    new_score=evaluate(new_sol)
    if new_score<score:
        sol=new_sol
        score=new_score
        