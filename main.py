from copy import copy
from random import choice
from typing import List
from Graph import Graph

def ND_algorithm_SI(G1: Graph, G2: Graph) -> bool:
    chosen_vertex_subgraph : dict[int,int]= {}
    marked_vertex_G1 : list = [False for i in range(G1.num_vertex)]
    #Chose
    for vertex in G2.vertex: 
        chose = choice(G1.vertex)
        #Verify
        if marked_vertex_G1[chose]:
            return False
        else:
            chosen_vertex_subgraph[vertex] = chose
            marked_vertex_G1[chose] = True
    #Verify
    for edge in G2.edges:
        fu = chosen_vertex_subgraph[edge[0]]
        fv = chosen_vertex_subgraph[edge[1]]
        if not G1.graph[fu][fv]:
            return False
    return True
    
        
# IClique = Input Clique; ISI = Input Subgraph Isomorphism
def ICLique_to_ISI(G: Graph, k : int) -> List[Graph]:
    vertex_G2 = [i for i in range(k)]
    edges_G2 = []
    for i in range(k):
        for j in range(k): #O(k^2)
            if j != i:
                edges_G2.append((i,j))
    G2 : Graph = Graph(vertex_G2,edges_G2) # Cria a matriz de adjacência
                                           # em O(|E|) = O(|V|^2) = O(k^2)
    return G,G2

def solveSI(G1 : Graph,G2 : Graph):
    used_columns = [False for i in range(G1.num_vertex)]
    curr_row = 0
    M = [[False for j in range(G1.num_vertex)] for i in range(G2.num_vertex)]
    return recursion(used_columns,curr_row,G1,G2,M)

def recursion(used_columns : list, curr_row :int,G1 : Graph,G2 : Graph, M: list):
    if curr_row == G2.num_vertex:
        mapp = is_isomorphism(M,G1,G2)
        if  mapp != None:
            return mapp
        else:
            return None
    
    for i in range(len(used_columns)):
        if not used_columns[i]:
            M[curr_row][i] = True
            used_columns[i] = True
            mapp = recursion(used_columns,curr_row + 1, G1,G2,M)
            if mapp != None:
                return mapp
            M[curr_row][i] = False
            used_columns[i] = False
    return None

def is_isomorphism(M:list,G1:Graph,G2:Graph):
    mapp : dict[int,int] = {}
    for i in range(G2.num_vertex):
        for j in range(G1.num_vertex):
            if M[i][j]:
                mapp[i] = j

    for edge in G2.edges:
        fu = mapp[edge[0]]
        fv = mapp[edge[1]]
        if not G1.graph[fu][fv]:
            return None
    return mapp


# OClique = Output Clique; OSI = Output Subgraph Isomorphism
def OSI_to_OCLique(mapp: dict[int,int]) -> list:
    return [v for k,v in mapp.items()] if mapp != None else []   
    # return list(mapp.values())

def verificationCLique(G1:Graph, k: int,vertex: list):
    if len(vertex) != k:
        return False
    for v1 in vertex:
        for v2 in vertex:
            if v1 != v2:
                if not G1.graph[v1][v2]:
                    return False
    return True
if __name__ == "__main__":
    vertex_G1 = [0,1,2,3]
    edges_G1 = [(0,1),(1,0),(0,3),(3,0),(1,3),(3,1),(1,2),(2,1)]
    G1 = Graph(vertex_G1,edges_G1)
    
    vertex_G2 = [0,1,2]
    edges_G2 = [(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)]
    G2 = Graph(vertex_G2,edges_G2)
    
    vertex_G3 = [0,1,2,3]
    edges_G3 = [(0,1),(1,0),(0,2),(2,0),(2,3),(3,2),(3,1),(1,3)]
    G3 = Graph(vertex_G3,edges_G3)
    # Validação das funções
    assert(solveSI(G1,G2) != None)
    
    while not ND_algorithm_SI(G1, G2):
        continue
    
    for i in range(1000000):
        assert(ND_algorithm_SI(G1, G3) == False)
    
    assert(solveSI(G1,G3) ==  None)
    
    assert(verificationCLique(G1,3,[0,1,3]) == True)
    assert(verificationCLique(G1,3,[0,1,2]) == False)
    # Execução da Redução
    k = 3
    # Mapeamento da Entrada
    G1,G2 = ICLique_to_ISI(G1,k)
    print("G1:")
    G1.print()
    print("G2:")
    G2.print()
    # Resolução do Problema
    mapp = solveSI(G1,G2)
    print("Output SI:",mapp)
    # Mapeamento da Saída
    OClique = OSI_to_OCLique(mapp)
    print("Output Clique:",OClique)
    # Verificação da saída
    assert(verificationCLique(G1,k,OClique) ==  True)
    
    