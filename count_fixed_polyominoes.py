import sys;

p = sys.argv[1]   # the current polyomino,
n = sys.argv[2]   # size of polyomino
c = 0             # countrer, starts from 0 

# MAKE GRAPH

g = {}

# nodes 
u = 0

for i in range(2-n,n):

    if  (i == 0):
        for j in range(0,n):
                nodes.insert(u,(i,j))
    elif  (i == n):
        for j in range(0,n):
                nodes.insert(u,(i,0))
        
    elif  (i == 2 - n):
        for j in range(0,1):
                nodes.insert(u,(i,1))
                
          
    elif (i > 0):
        for j in range(0,n - i):
                nodes.insert(u,(i,j))
        
    elif i < 0: 
        for j in range(1,n+i):
            nodes.insert(u,(i,j))
                
nodes.sort()

#neighbors



for i in nodes.items():

    for value in nodes.items():

        if ((i,j+1) in nodes.key():
            g[nodes].append(nodes(i,(i,J+1))

        if ((i,j-1) in nodes.key():
            g[nodes].append(nodes(i,(i,j-1))
            
        if ((i+1,j) in nodes.key():
            g[nodes].append(nodes(i,(i+1,j)

        if ((i-1,j) in nodes.key():
            g[nodes].append(nodes(i,(i-1,j))
            
    
g[nodes].sort()

untried = {} # make set untried
untried = {(0,0)}# start untried with (0,0)

# DEFINE METHODS 

def isSetΕmpty(untried):
    if (len(untried) == 0):
        return True
    else
        return False

def RemoveFromSet(untried):

    u = untried.pop() # removed item
    return u


def AppendtoList(p,u):
    p.append(u) 
   

def RemoveFromList(p,u):
    p.remove(u)

def ValueOf(c): 
    return c 

def AddOne(c):
    c = c + 1
    return c

def Neighbors(p/u)):
    for i in p:
        if p[i] == u 
            break;
            return[]

        else 
            return g[i]


new_neighbors = {}

def AddtoSet(new_neighbors,u):
    new_neighbors.add(g[u])
    
p = []

# ALGORYTHM 

def CountFixedPolyominoes(G,untried,n,p,c):


    while not (isSetΕmpty(untried)): { # true or false 
    
        u = RemoveFromSet(untried)
        AppendtoList(p,u)
        if (len(p) == n):
            AddOne(c)
        else :
            new_neighbors = {}
            for v in g[nodes]:
                if((v not in untried.items():
                    continue
                if( v not in p.items)):
                    continue 
                if (v not in Neighbors(p/u)): 
                    continue
                    AddtoSet(new_neighbors,u)
                    untried.add(new_neighbors)
            CountFixedPolyominoes(G,untried,n,p,c)

         RemoveFromList(p,u)
    return ValueOf(c)
}
    
# PRINT
 
if  (p != "-p"):
    print(ValueOf(c))
else 
    for i in range(0,len(g))
    print(g[i])
    print c
