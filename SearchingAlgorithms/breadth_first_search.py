class undirected_graph_node:
    def __init__(self, num):
        self.val = num
        self.nbr = []


def bfs(node):
    """
    Breadth-first search is an algorithm for traversing graph(or tree) data structure.
    It starts at a given start node and explores the neighbor nodes first (where the name comes from),
    before moving to the next level neighbors. <From Wikipedia>
    pseudocode:
    - initialize a queue (qu) [FIFO a key for bfs]
    - initialize a set (visited)
    - add the given start node to qu
    - add the given start node to visited
    - while qu is not empty, repeat:
        - current_node = qu.pop()
        - print current_node (or can do some other operation)
        - for each nbr of current_node, repeat:
            - if nbr is not in visited:
                - add nbr to visited
                - add nbr to qu
    - end
    """
    qu = []
    visited = set()
    qu.insert(0, node)
    visited.add(node)
    while qu:
        cur_node = qu.pop()
        print cur_node.val
        for nbr in cur_node.nbr:
            if nbr not in visited:
                visited.add(nbr)
                qu.insert(0, nbr)
    return

if __name__ == '__main__':
    """
    implement bfs on an undirected_graph:
          1 - 3    
         / \
        2   4
         \ / \
          6   5
    """
    node1 = undirected_graph_node(1)
    node2 = undirected_graph_node(2)
    node3 = undirected_graph_node(3)
    node4 = undirected_graph_node(4)
    node5 = undirected_graph_node(5)
    node6 = undirected_graph_node(6)
    node1.nbr += [node2, node3, node4]
    node2.nbr += [node1, node6]
    node3.nbr += [node1]
    node4.nbr += [node1, node5, node6]
    node5.nbr += [node4]
    node6.nbr += [node2, node4]
    print "bfs starting from node 1"
    bfs(node1)
    print "bfs starting from node 2"
    bfs(node2)
    print "bfs starting from node 3"
    bfs(node3)
    print "bfs starting from node 4"
    bfs(node4)
    print "bfs starting from node 5"
    bfs(node5)
    print "bfs starting from node 6"
    bfs(node6)
