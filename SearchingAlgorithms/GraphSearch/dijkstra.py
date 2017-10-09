import heapq

data = {
    "Oradea": {"conn": [("Zerind", 71), ("Sibiu", 151)]}
    ,"Zerind": {"conn": [("Oradea", 71), ("Arad", 75)]}
    ,"Arad": {"conn": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)]}
    ,"Timisoara": {"conn": [("Arad", 118), ("Lugoj", 111)]}
    ,"Lugoj": {"conn": [("Timisoara", 111), ("Mehadia", 70)]}
    ,"Mehadia": {"conn": [("Lugoj", 70), ("Drobeta", 75)]}
    ,"Drobeta": {"conn": [("Mehadia", 75), ("Craiova", 120)]}
    ,"Craiova": {"conn": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)]}
    ,"Sibiu": {"conn": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)]}
    ,"Fagaras": {"conn": [("Sibiu", 99), ("Bucharest", 211)]}
    ,"Rimnicu Vilcea": {"conn": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)]}
    ,"Pitesti": {"conn": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)]}
    ,"Bucharest": {"conn": [("Pitesti", 101), ("Fagaras", 211), ("Giurgiu", 90), ("Urziceni", 85)]}
    ,"Giurgiu": {"conn": [("Bucharest", 90)]}
    ,"Urziceni": {"conn": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)]}
    ,"Hirsova": {"conn": [("Urziceni", 98), ("Eforie", 86)]}
    ,"Eforie": {"conn": [("Hirsova", 86)]}
    ,"Vaslui": {"conn": [("Urziceni", 142), ("Iasi", 92)]}
    ,"Iasi": {"conn": [("Vaslui", 92), ("Neamt", 87)]}
    ,"Neamt": {"conn": [("Iasi", 87)]}
}

def dijkstra(db, frm, to):
    # Input sanity check
    if frm is to or frm not in db or to not in db:
        return []

    # Init internal data structure
    queue = []
    heapq.heappush(queue, (0, (frm, [frm])))

    # Set datastore objects to visited
    selected = {frm: {"state": "start", "route": [frm], "dist": 0},
                to: {"state": "goal", "route": [to], "dist": 0}}

    # Start routing with two processes until reaching a common point
    while queue:
        # Get the vertex with the lowest distance (highest priority in the queue)
        (dist, (location, route)) = heapq.heappop(queue)

        # If the goal is found then return the route
        if location in selected and selected[location]["state"] is "goal":
            return {"dist": selected[location]["dist"] + dist,
                    "route": route[:-1:] + selected[location]["route"][::-1]}
        # If the vertex has not been visited yet add it to visited ones
        elif location not in selected:
            selected[location] = {"state": "visited", "route": route, "dist": dist}

        # Take all connected vertices and add them to the queue
        for (cLocation, cDist) in db[location]["conn"]:
            # Check if vertex has already not yet been used
            # Goal check is done since the goal is in selected from the beginning on
            if cLocation not in selected or selected[cLocation]["state"] is "goal":
                # Add to be processed later
                heapq.heappush(queue, (dist + cDist, (cLocation, route + [cLocation])))

    return {"error": "No route found!"}

dijkstra(data, "Oradea", "Neamt")
