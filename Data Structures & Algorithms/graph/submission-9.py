from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {}
    


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []

        self.graph[src].append(dst)




    def removeEdge(self, src: int, dst: int) -> bool:
        
        try:
            if dst not in self.graph[src]:
                return False
        
            else:
                self.graph[src].remove(dst)
                return True
        except: 
            return False


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.bfs(src, dst, visited)


    def bfs(self, src, dst, visited):
        queue = deque()
        

        queue.append(src)

        while queue:
            layer = queue.pop() #pop 1
            visited.add(layer)

            
            for path in self.graph[layer]:
              
                if path == dst:
                    return True
                elif path not in queue and path not in visited:
                    queue.append(path)
               
        return False





                

            
        
        



