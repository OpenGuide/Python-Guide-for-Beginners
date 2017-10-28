graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
         }

# here A,B,....,F represents each node and nodes inside set are the one which are connected with main node


def bfs_paths(graph, start, goal):
    """
    :param graph: complete nodes and vertices are given
    :param start: Starting point
    :param goal: Ending point
    :return: shortest path for the given graph
    """

    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

if __name__ == '__main__':

    result = shortest_path(graph, 'A', 'F')
    print "shortest path is: ", ' -> '.join(result)