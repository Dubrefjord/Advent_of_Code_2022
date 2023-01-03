import re
from queue import PriorityQueue

graph = {}
flows = {}
def main():
    global graph; global flows
    root = 'AA'

    # build graph
    for line in open('input16.txt'):
        data = re.findall(r"[A-Z]{2}", line)
        flow = re.findall(r"(\d+)",line)
        for i in data[1:]:
            add_edge(node1=data[0], node2=i, cost=1)
        flows[data[0]] = int(flow[0])

    # minimize graph by removing nodes with flow = 0, increasing weights instead
    graph_copy = dict(graph)
    for node in graph_copy:
        if flows[node] == 0 and node != root:
            remove_node(node)
            graph.pop(node)

    # ∀ node in G create shortest path tree and add edges. 
    # Add 1 to all edges for opening valve. No need to deal with root not being a valve-node since 
    # in my solution each node will be visited at most once, and we start with root already visited.
    for node in graph:
        graph[node] = (shortest_path_tree_distances(node, graph))
  
    for node in graph:
        for idx,(neighbor,weight) in enumerate(graph[node]):
            graph[node][idx] = (neighbor , weight+1)

    print(find_highest_pressure(graph,root,30))


# pqFS (prio efter nodens flow), spara path och spara högsta pressure so far.
# If nuvarande path inte kan komma upp i samma pressure (antag kvarvarande noder i fallande ordning. Gör aritmetrisk summa där vi antar att avstånd mellan alla noder är 2.) så kan vi kapa den grenen helt!
# => Borde göra gigantisk skillnad när vi har många noder, slippa fakultetkomplexitet! :heart:
# prioqueue så att vi börjar med att testa paths med göttigaste noderna så tidigt som möjligt. Leder till att vi kan skippa paths enl ovan tidigt!

def find_highest_pressure(graph, root, limit):
    pq = PriorityQueue()
    pq.put((0, 0, 0, root, [])) # (-flow[node]*(limit-time_passed), time, pressure, node, path). Negative flow because pq returns smallest first. Could write an object to put in the pq and define its __lt__ function to get around this.
    max_pressure = (0,0, [root]) # pressure, time_passed, path
    skipped = 0; processed = 0

    while not pq.empty():
        _, time_passed, pressure, node, path = pq.get()
        pressure += flows[node]*(limit-time_passed)
        processed += 1
        # check if this branch could possibly get a higher pressure than max_pressure. Else continue.
        if max_possible_pressure(time_passed, pressure, limit, path) > max_pressure[0]:
            path = path[:]
            path.append(node)
            if pressure > max_pressure[0]:
                max_pressure = (pressure, time_passed, path)

            for neighbor,weight in graph[node]:
                time_after_traverse = time_passed + weight
                if time_after_traverse <= limit and neighbor not in path:
                    pq.put((-flows[neighbor], time_after_traverse, pressure, neighbor, path))
        else:
            skipped += 1
    
    print('partly processed nodes, where branch was skipped = ',skipped)
    print('fully processed nodes = ',processed-skipped)
    return max_pressure # TODO Felsök. Vad kan vara fel?


def max_possible_pressure(time_passed, pressure, limit, path):
    for flow in sorted([flows[node] for node in (set(graph.keys()) - set(path))], reverse=True):
        time_passed += 2
        if time_passed > limit: break
        pressure += flow*(limit+1-time_passed)
    return pressure
        

def shortest_path_tree_distances(start_node, graph): #shortest_path_tree_dist returns [(id,w),..]
    #Add all neighbor id,weight to list iff weight less than current in list. If node A has its weight updated, we want to check A's neighbors for updating too. Add to queue
    shortest_path = {}
    for node in graph:
        shortest_path[node] = 20000
    shortest_path[start_node] = 0

    pqueue = PriorityQueue() #low first
    pqueue.put((0,start_node))

    while not pqueue.empty():
        (distance, node) = pqueue.get()
       
        for neighbor,_ in graph[node]:
            if distance + weight_from_to(node,neighbor) < shortest_path[neighbor]:
                shortest_path[neighbor] = distance + weight_from_to(node,neighbor)
                pqueue.put((shortest_path[neighbor],neighbor))
    shortest_path.pop(start_node)

    return list(shortest_path.items())
            

def add_edge(node1, node2, cost = 1000):
    global graph

    if node1 not in graph: graph[node1] = []
    if node2 not in graph: graph[node2] = []

    graph[node1].append((node2, cost))


def remove_edge(node1,node2):
    graph[node1] = [x for x in graph[node1] if x[0] != node2]


def remove_node(node):
    global graph
    neighbors = graph[node]
    
    #ta bort node ur neighbors lista, lägg till alla nodes neighbors med vikt om väg med lägre vikt inte redan existerar hos neigbor
    for neighbor1,weight1 in neighbors:
        for neighbor2,weight2 in neighbors:
            if neighbor1 == neighbor2: continue
            
            weight_from_n1 = weight_from_to(neighbor1,node)
            # if not n1->n2 or n1->n2.w >weight1+weight2: add to n1: (n2,weight1+weight2) and n2: (n1,weight1+weight2)
            ######               TODO:below             ##########
            # Olika vikter på olika håll! Kan inte köra weight1+weight2. n1->n2 = w(n1,n)+w(n,n2) och vice versa
            if not neighbor_weight(neighbor1,neighbor2) or neighbor_weight(neighbor1,neighbor2) > weight_from_n1+weight2:
                add_edge(neighbor1,neighbor2, weight_from_n1+weight2)
            remove_edge(neighbor1,node)


def weight_from_to(node1,node2):
    weight_from_n1=2000
    for id,w in graph[node1]:
        weight_from_n1 = w if id == node2 else weight_from_n1
    return weight_from_n1


def neighbor_weight(node1,node2):
    global graph
    # if not neighbors return false else return weight
    for id,w in graph[node1]:
        if id == node2:
            return w
    return False

        
        
        


if __name__ == "__main__":
    main()

