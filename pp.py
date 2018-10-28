Vertice = 4
NP = 99999
def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(Vertice):
        for i in range(Vertice):
            for j in range(Vertice):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    printSolution(dist)
def printSolution(dist):
    print("The shortest distance between every pair of vertices: ")
    for i in range(Vertice):
        for j in range(Vertice):
            if (dist[i][j] == NP):
                print("%7s" % ("NP"),)
            else:
                print("%7d\t" % (dist[i][j]),)
            if j == Vertice - 1:
                print("")

"""To test the above program Let us create the following weighted graph

            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           """
graph = [[0, 5, NP, 10],
         [NP, 0, 3, NP],
         [NP, NP, 0, 1],
         [NP, NP, NP, 0]
         ]
# Print the solution
floydWarshall(graph)
