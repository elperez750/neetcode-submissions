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
        if (src) not in self.graph or dst not in self.graph:
            return False
        else:
            self.graph[src].remove(dst)
            return True


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.bfs(src, dst, visited)

        

    def bfs(self, src, dst,  visited):
        queue = deque()

        #1 will be added to the queue and visited
        visited.add(src)
        queue.append(src)


        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node)
                neighbors = self.graph[node]
                if node == dst:
                    return True
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                    else:
                        continue

        return False
                






        

