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
            print(j), 
            return 0 
        l = self.printPath(parent , parent[j]) 
   
        Path_len = l + Path_len 
 
        if j < self.V_org :  
            print(j), 
  
        return Path_len 
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
    g.addEdge(int(i[1]),int(i[0]), int(i[2])) 
 
src = int(input('Введите начальную вершину\n')); dest = int(input('Введите конечную вершину\n'))
print ("Кратчайший путь между %d и %d   " %(src, dest)), 
l = g.findShortestPath(src, dest) 
 
  
