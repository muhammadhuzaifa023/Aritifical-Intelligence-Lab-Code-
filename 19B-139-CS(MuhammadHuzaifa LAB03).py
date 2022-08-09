# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:57:40 2022

@author: muham
"""





#Task 1
#Solve 8- Puzzle problem:
#• Consist of 3 × 3 board with eight numbered tiles and a blank space.
#• A tile adjacent to the blank space can slide into the space.
#• The objective is to reach a specified goal state, such as the one shown in the discussion above.
import copy 
state=[0,1,2,3,4,5,6,7,8]

def move_right(board):
    board=copy.deepcopy(board)
    zero_index=board.index(0)
    if zero_index==2 or zero_index==5 or zero_index==8:
        return(board)
    board[zero_index],board[zero_index+1]=board[zero_index+1],board[zero_index]
    return(board)

def move_left(board):
    board=copy.deepcopy(board)
    zero_index=board.index(0)
    if zero_index==0 or zero_index==3 or zero_index==6:
        return(board)
    board[zero_index],board[zero_index-1]=board[zero_index-1],board[zero_index]
    return(board)
def move_up(board):
    board=copy.deepcopy(board)
    zero_index=board.index(0)
    if zero_index>5:
        return(board)
    board[zero_index],board[zero_index+3]=board[zero_index+3],board[zero_index]
    return(board)

def move_down(board):
    board=copy.deepcopy(board)
    zero_index=board.index(0)
    if zero_index<3:
        return(board)
    board[zero_index],board[zero_index-3]=board[zero_index-3],board[zero_index]
    return(board)



def generate_child(board):
    return(move_right(board), move_left(board),move_up(board),move_down(board))


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)
def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), node, "move_up", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_down(node.state), node, "move_down", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_left(node.state), node, "move_left", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_right(node.state), node, "move_right", node.depth + 1, 0))
    expanded_nodes = [node for node in expanded_nodes if node.state != None] 
    return expanded_nodes
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.heuristic=None
def BFS(Initial,Final):
    
    goal=Final
    start_node=create_node(Initial,None,None,0,0)
    fringe=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    path=[]
    while(current.state!=goal):
        fringe.extend(expand_node(current))
        current=fringe.pop(0)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent
    return path



print(BFS([1,2,3,5,6,0,7,8,4],[1,2,3,5,8,6,0,7,4]))



print("-"*50)
#Task2
#Solve depth first search and breadth first search of following graph starting from node A and reaching goal node G:
    
    

# BFS 
def BFS(graph,Initial,goal):
    fringe=[]
    fringe.append([Initial])
    
    while fringe:
        path=fringe.pop(0)
        node=path[-1]
        if node ==goal:
            return path
        child=[]
        if node in graph:
            child=graph[node]
        for item in child:
            new_path=copy.deepcopy(path)
            new_path.append(item)
            fringe.append(new_path)
    return 'failure'
print("BFS")
Graph={'A':['B','D'],'B':['E','C'],'D':['E','G','H'],'E':['F']}
print(BFS(Graph,'A','G'))

print("-"*50)   
def DFS(graph,Initial,goal):
    fringe=[]
    fringe.append([Initial])
    
    while fringe:
        path=fringe.pop(0)
        node=path[-1]
        if node ==goal:
            return path
        child=[]
        if node in graph:
            child=graph[node]
        for item in child:
            new_path=copy.deepcopy(path)
            new_path.append(item)
            fringe.insert(0,new_path)
    return 'failure'
print("DFS")
Graph={'A':['B','D'],'B':['E','C'],'D':['E','G','H'],'E':['F']}
print(DFS(Graph,'A','G'))

 