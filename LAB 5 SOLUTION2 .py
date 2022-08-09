


import copy

def compute_cost(graph,path):
    actual_path=path[0]
    cost=0
    for i in range(len(path[0])-1):
        cost+=graph[actual_path[i]][actual_path[i+1]]
    return cost
def a_star1(graph,initial,goal,heuristic):
    
    fringe=[]
    visited=[]
    fringe.append([[initial],0+heuristic[initial]])
    
    while len(fringe)!=0:
        path=fringe.pop(0)
        node=path[0][-1]
        if node==goal:
            #print(path)
            return path,compute_cost(graph,path)
        child=[]
        visited.append(node)
        if node in graph:
        
            child=graph[node]
            
        for item in child:
            if item in visited:
                continue
            new_path=copy.deepcopy(path)
            new_path[0].append(item)
            new_path[-1]=compute_cost(graph,new_path)+heuristic[item] #f(n)=g(n)+h(n)
            fringe.append(new_path)
        fringe.sort(key=lambda x:x[1])
            
    return 'Failure'



heuristic1 = {
             'Arad':366,
             'Bucharest':0,
             'Craiova':160,
             'Dobreta':242,
             'Eforie':161,
             'Fagaras':176,
             'Giurgiu':77,
	     'Hirsova':151,
	     'Iasi':226,
	     'Lugoj':244,
	     'Mehadia':241,
	     'Neamt':234,
	     'Oradea':380,
	     'Pitesti':10,
	     'Rimnicu_Vilcea':193,
	     'Sibiu':253,
	     'Timisoara':329,
	     'Urziceni':80,
	     'Vaslui':199,
	     'Zerind':374		
             }
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu_Vilcea': 80},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu_Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Craiova': {'Pitesti': 138, 'Rimnicu_Vilcea': 148, 'Dobreta': 120},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu_Vilcea': 97},
    'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 88},
    'Eforie': {'Hirsova': 88}
}
a=a_star1(graph,'Arad','Giurgiu',heuristic1)

def a_star2(graph,initial,goal,heuristic):
    
    fringe=[]
    visited=[]
    fringe.append([[initial],0+heuristic[initial]])
    
    while len(fringe)!=0:
        path=fringe.pop(0)
        node=path[0][-1]
        if node==goal:
            #print(path)
            return path,compute_cost(graph,path)
        child=[]
        visited.append(node)
        if node in graph:
        
            child=graph[node]
            
        for item in child:
            if item in visited:
                continue
            new_path=copy.deepcopy(path)
            new_path[0].append(item)
            new_path[-1]=compute_cost(graph,new_path)+heuristic[item] #f(n)=g(n)+h(n)
            fringe.append(new_path)
        fringe.sort(key=lambda x:x[1])
            
    return 'Failure'




heuristic2 = {
    'Arad': 370,
    'Bucharest': 20,
    'Craiova': 40,
    'Dobreta': 50,
    'Eforie': 151,
    'Fagaras': 276,
    'Giurgiu': 177,
    'Hirsova': 121,
    'Iasi': 326,
    'Lugoj': 167,
    'Mehadia': 211,
    'Neamt': 250,
    'Oradea': 180,
    'Pitesti': 110,
    'Rimnicu_Vilcea': 293,
    'Sibiu': 240,
    'Timisoara': 300,
    'Urziceni': 480,
    'Vaslui': 199,
    'Zerind': 374
}

b=a_star2(graph,'Arad','Giurgiu',heuristic2)
#b=a_star2(graph,'Arad','Giurgiu',heuristic2)
def Comparison_heuristics(a,b):
    if (a[0][1]<b[0][1]):
        print("Heristics1 is small than Heristics2 that why we follow this path: ")
        return(a_star1(graph,'Arad','Giurgiu',heuristic1))
    

    else:
        print("Heristics2 is small than Heristics1 that why we follow this path")
        return(a_star2(graph,'Arad','Giurgiu',heuristic2))
print(Comparison_heuristics(a,b))