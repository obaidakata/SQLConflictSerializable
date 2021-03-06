class DirectedGraph:
    adjacencyLists = {}

    def __init__(self, vertices):
        for vertex in vertices:
            self.adjacencyLists[vertex] = []

    def addEdge(self, firstVertex, secondVertex):
        if firstVertex in self.adjacencyLists.keys():
            if secondVertex not in self.adjacencyLists[firstVertex]:
                self.adjacencyLists[firstVertex].append(secondVertex)
        else:
            print("Error 1")

    def topologicalSort(self):
        queue = []
        outputList = []
        inDegree = {}
        str = ''
        for vertex in self.adjacencyLists:
            inDegree[vertex] = 0

        for u in self.adjacencyLists:
            for v in self.adjacencyLists[u]:
                inDegree[v] = inDegree[v] + 1

        for vertex in self.adjacencyLists:
            if inDegree[vertex] == 0:
                queue.append(vertex)

        while len(queue) != 0:
            v = queue.pop()
            outputList.append(v)
            for u in self.adjacencyLists[v]:
                inDegree[u] = inDegree[u] - 1
                if inDegree[u] == 0:
                    queue.append(u)

        for vertex in self.adjacencyLists:
            if inDegree[vertex] != 0:
                print("No, cycle detected")
                return False

        for x in outputList:
            str += "T{0} ".format(x)
            if x != outputList[-1]:
                str += "-> "
        print(str)

        return True
