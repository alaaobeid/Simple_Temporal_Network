# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:46:31 2020

@author: Aladdin Tahir
"""

import sys
import numpy as np

#-----------#
# STN class #
#-----------#

class STN:

    ## useful maximum upper bound
    inf = sys.float_info.max

    ## list of nodes and adjacency list        
    nodes = []
    adj_list = {}
    
    
#-------------#
# Main method #
#-------------#

def main():
    def adj_list_to_matrix(adj_list):
        n = len(adj_list)
        ## set all self distances to 0
        adj_matrix = np.inf * np.ones((n,n))

        ## set missing distances to infinity
        np.fill_diagonal(adj_matrix,0)

        for i ,children in enumerate( adj_list.values()):
            # print( children ,i)
            for k, w in children.items():

                j = getIndexOf( adj_list.keys() , k)
            # print( i , j , k, w)
                adj_matrix[i,j] = w
        return adj_matrix

    def getIndexOf( stack , index):

        for i,j in enumerate(stack):
            if( j == index):
                return i
    
        return None
    ## TODO print STN in DOT form
    def print_stn(self):
        print("digraph plan {")
        for node1 in range(V):
            for node2 in range(V):
                if self[node1][node2] != 0 and self[node1][node2]<stn.inf:
                    print(stn.nodes[node1]," -> ",stn.nodes[node2],"[ label=", self[node1][node2],"]")
        
        
        # print all node names, one per line
        # print all edges, one per line in format:
        #  <souce> -> <sink> [ label="<bound>" ];
        print ("}")
    ## TODO check the consistency of the STN
    def check_consistency(graph):
        V=len(graph)
        dist = graph
        for k in range(V): 
            for i in range(V): 
                for j in range(V): 
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            if i == j and dist[i][j] <0:
                                print("GRAPH IS INCONSISTENT")
                                sys.exit()
        return dist


    ## TODO remove dominated edges from the STN
    def make_minimal(self):
        dist=self
        for k in range(V):
            for j in range(V):
                for i in range(V):
                    try:
                        if i != j and j != k and i != k:
                            if dist[i][j] > 0 and dist[k][j] > 0 and dist[i][j] == dist[k][j] + dist[i][k]:
                                dist[i][j] = stn.inf
                            elif dist[i][j] < 0 and dist[i][k] < 0 and dist[i][j] == dist[k][j] + dist[i][k]:
                                dist[i][j] = stn.inf
                        
                    except:
                        pass
        return dist
            
        # Use triangle inequality to remove dominated edges from the graph.
        # Be careful not to remove too many edges!
        return self.adj_list
    ## open the DOT file
    with open(sys.argv[1], "r") as dotfile:

        stn = STN()
        list=[]
        list_no=[]

        for line in dotfile:

            ## read edge
            if "->" in line:
                node1 = line[0:line.index('->')-1].strip()
                node2 = line[line.index('->')+2:line.index('[')-1].strip()
                if node1 not in list:
                    list.append(node1)
                if node2 not in list:
                    list.append(node2)
                number = line[line.index('="')+2:line.index('" ')].strip()
                list_no.append(number)
                stn.adj_list
                if node1 not in stn.adj_list:
                    stn.adj_list[node1] = {node2:number}
                if node2 not in stn.adj_list[node1]:
                    stn.adj_list[node1][node2] = number
                for i in list:
                    if i not in stn.adj_list:
                        stn.adj_list[i] = {}
                    
                continue
        stn.nodes=list
        for n in stn.adj_list.keys():
            stn.adj_list[n][n] = 0
            for i in stn.nodes:
                if i not in stn.adj_list[n]:
                    stn.adj_list[n][i]= stn.inf
        ## TODO set missing distances to infinity
        #print(stn.print_stn())
        ## Check consistency, make minimal, and print!
        
        
        adj_matrix=adj_list_to_matrix(stn.adj_list)
        V=len(adj_matrix)
        adj_matrix=check_consistency(adj_matrix)
        h=make_minimal(adj_matrix)
        print_stn(h)
            

if __name__ == '__main__':
    main()