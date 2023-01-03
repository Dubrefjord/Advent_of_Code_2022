from collections import deque

def main():
    input = open('input12.txt').readlines()
    graph = {}
    start = tuple([(y,line.index('S')) for y,line in enumerate(input) if 'S' in line][0])
    end = tuple([(y,line.index('E')) for y,line in enumerate(input) if 'E' in line][0])

    for y,line in enumerate(input):
        line = line.strip()
        if 'S' in line:
            line = line.replace('S','a')
        if 'E' in line:
            line = line.replace('E','z')
        input[y] = line


    for y, line in enumerate(input):
        for x, _ in enumerate(line):
            arcs = []
            if x >= 1:
                arcs.append((y,x-1)) if ord(input[y][x-1]) >= ord(input[y][x])-1 else None
            if x < len(line)-1:
                arcs.append((y,x+1)) if ord(input[y][x+1]) >= ord(input[y][x])-1 else None
            if y >= 1:
                arcs.append((y-1,x)) if ord(input[y-1][x]) >= ord(input[y][x])-1 else None
            if y < len(input)-1:
                arcs.append((y+1,x)) if ord(input[y+1][x]) >= ord(input[y][x])-1 else None
            graph[(y,x)] = arcs

    print(len(flatten_list(find_shortest_path_to_value(input,graph,end,'a'),[]))-1)

def find_shortest_path(graph,start,end):
    queue = deque([start])
    dist = {start: [start]}
    while len(queue):
        node = queue.pop()
        for next in graph[node]:
            if next not in dist:
                dist[next] = [dist[node],next]
                queue.appendleft(next)
    return dist.get(end)

def find_shortest_path_to_value(landscape,graph,start,val):
    queue = deque([start])
    dist = {start: [start]}
    while len(queue):
        node = queue.pop()
        for next in graph[node]:
            if next not in dist:
                dist[next] = [dist[node],next]
                queue.appendleft(next)
                (y,x) = next
                if landscape[y][x] == val:
                    return dist.get(next)
    return None


def flatten_list(data,flat_list):
    for element in data:
        if type(element) == list:
            flatten_list(element,flat_list)
        else:
            flat_list.append(element)
    return flat_list


if __name__ == "__main__":
    main()
