from collections import defaultdict 
class Graph: 
   
    def __init__(self,vertices): 
        self.V = vertices
        self.V_org = vertices 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v,w): 
        if w == 1: 
            self.graph[u].append(v) 
        else:    
            self.graph[u].append(self.V) 
            self.graph[self.V].append(v) 
            self.V = self.V + 1
    def printPath(self, parent, j): 
        Path_len = 1
        if parent[j] == -1 and j < self.V_org :
            path.append(j)
            return 0 
        l = self.printPath(parent , parent[j]) 
   

        if j < self.V_org :  
            path.append(j) 
 
  
 
  
        return path 
    def findShortestPath(self,src, dest): 
  
        visited =[False]*(self.V) 
        parent =[-1]*(self.V) 
   
        queue=[] 
  
        queue.append(src) 
        visited[src] = True
   
        while queue : 
             
            s = queue.pop(0) 
              
            
            if s == dest: 
                return self.printPath(parent, s) 
                  
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                    parent[i] = s 
   
path_dict={} 
path = []
user_input = eval(input('Введите ребра: '))
v = []
for i in user_input:
    if not (i[0] in v):
        v.append(i[0])
        if not(i[1] in v):
            v.append(i[1])
    elif not(i[1] in v):
        v.append(i[1])
g = Graph(len(v)) 
for i in user_input:
    g.addEdge(int(i[0]),int(i[1]), int(i[2]))
    path_dict[str(i[0])+'-'+str(i[1])]= int(i[2])
    path_dict[str(i[1])+'-'+str(i[0])]= int(i[2])
    g.addEdge(int(i[1]),int(i[0]), int(i[2])) 

src = int(input('Введите узел\n'))
i = 0
flag = 0
while i < len(v):
    dest = i
    l = g.findShortestPath(src,dest)
    path = []
    if l == None :
        flag = 1
    i +=1 
if flag:
    print(-1)
else:
    maxp = 0
    i = 0
    while i < len(v):
        dest = i
        print(i)
        l = g.findShortestPath(src,dest)
        weight = 0
        j = 0
        while j < (len(path)-1):
            print(path)
            weight += path_dict[str(j)+'-'+str(j+1)]
            j+=1
        print(weight)
        if weight > maxp :
            maxp = weight
        path = []
        i+=1
    print(maxp)





















  
