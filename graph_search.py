from collections import defaultdict 
class Graph: 
  
    def __init__(self): 
  
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 

        visited = [False] * (len(self.graph)) 
  
        queue = [] 
  
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            s = queue.pop(0) 
            print (s, end = " ") 

            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
    def DFSUtil(self, v, visited): 

        visited[v] = True
        print(v, end = ' ') 
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    def DFS(self, v): 
  

        visited = [False] * (len(self.graph)) 
  

        self.DFSUtil(v, visited) 
user_input = eval(input('Введите ребра: '))
g = Graph() 
for i in user_input:
    g.addEdge(int(i[0]),int(i[1]))
    g.addEdge(int(i[1]),int(i[0]))
k = 0
k = input('Введите начальную вершину:')
print('Обход в ширину : ')
g.BFS(int(k))
print('\n') 
print('Обход в глубину : ')
g.DFS(int(k))
print('\n')