import copy
import random
class chromosome:
    def __init__(self):
        self.x=random.randint(-5,5)
        self.y=random.randint(-5,5)
        self.fitness=self.evaluate()
#evaluate the fitness according to the function x**2+y**2

    def evaluate(self):
        return (pow(self.x,2)+pow(self.y,2))
#parent selection 
class selection:
    #randomly ek parent return kraygaa
    def rand_parent(pop):
        index=random.randint(0,len(pop)-1)
        print(index)
        indivi=copy.deepcopy(pop[index])
        #indivi=random.choice(pop)
        print(indivi)
        print("***",indivi.x,indivi.y,indivi.fitness)
        
        return(indivi)
    #selecting the best parenrts for poplutaion
    def trunc(pop):
        sorted_pop=sorted(pop,key=lambda x:x.fitness,reverse=True)
        #print(sorted_pop)
        #print(sorted_pop[0],sorted_pop[1],sorted_pop[2])
        return sorted_pop[0],sorted_pop[1]
    def trunc_pop(pop):#top most parent select kerlayga
        sorted_pop=sorted(pop,key=lambda x:x.fitness,reverse=True)
        return sorted_pop[:10]
        
#child create ker raha hoo
class operator:
    #Order 1 cross over / or we say that two point cross over 
    #(5,5) and (-1,3) parents 
    #After onepoint cossover to produce children 
    #Here we same the x but different the y 
    #so after cross over (5,3) and (-1,5)
    
    def one_point(parent1,parent2):
        child1=copy.deepcopy(parent1)
        child2=copy.deepcopy(parent2)
        child1.y=parent2.y
        child2.y=parent1.y
        child1.fitness=child1.evaluate()
        child2.fitness=child1.evaluate()
        return child1,child2
    #mutation in child minute changes
    def uniform_mutation(child):
        #random.random o say 1 ka beech may number dyta haii probability 
        if random.random()< .5:#aghr x hai ya y haii 
            if random.random() < .5: # coin toss whether the probability is less than .5 than mutation in x
                if child.x > 4.5:
                    pass
                else:
                    child.x+=5 #increment +5
            else:
                if child.x < 4.5:
                    pass
                else:
                    child.x-=.5
        else:
             if random.random() < .5:
                if child.y> 4.5:
                    pass
                else:
                    child.y+=5
             else:
                if child.y < 4.5:
                    pass
                else:
                    child.y-=.5
                
        child.fitnes=child.evaluate()
        return child