def dijkstra(graph, start, finish):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph

    infinity = 9999999
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = finish
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[finish] != infinity:
        print('Shortest distance is ' + str(shortest_distance[finish]))
        print('And the path is ' + str(path))


def testDijkstra():
    graph = {
        'S': {'P': 1, 'E': 9, 'D': 3},
        'P': {'S': 1, 'Q': 15, 'H': 4},
        'Q': {'P': 15, 'H': 4},
        'D': {'S': 3, 'E': 2, 'B': 1, 'C': 8},
        'H': {'P': 4, 'Q': 4, 'E': 8},
        'E': {'D': 2, 'S': 9, 'R': 2, 'H': 8},
        'A': {'B': 2, 'C': 2},
        'B': {'A': 2, 'D': 1},
        'C': {'A': 2, 'D': 8, 'F': 3},
        'R': {'E': 2, 'F': 2},
        'F': {'R': 2, 'G': 2, 'C': 3},
        'G': {'F': 2}
    }

    start = 'S'
    finish = 'G'

    print(start + " -> " + finish)
    dijkstra(graph, start, finish)
    print()


def main():
    testDijkstra()


if __name__ == "__main__":
    main()