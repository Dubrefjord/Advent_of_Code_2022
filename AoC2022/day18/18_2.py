from queue import PriorityQueue
# Trying to figure out where the cavities are sounds hard! Probably easier to go over the outside and count all of the sides.
# Not that that way sounds easy....
# Pathfinding from each neighbor node to origo (or some point outside the cluster) pq = (dist to node in outside-set, )                             nl
import time

cubes = set()
outside = set()
inside = set()
def main(): 
    start_time = time.time()
    sides = 0
    # parse data, create cubes
    for line in open('input18.txt').readlines():
        line = line.strip().split(',')
        cubes.add((int(line[0]),int(line[1]),int(line[2])))
        outside.add((0,0,0))

    for x,y,z in cubes:
        for xn,yn,zn in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
            if (xn,yn,zn) not in cubes:
                sides += pathfind_origo((xn,yn,zn))

    print("--- %s seconds ---" % (time.time() - start_time))
    print(sides)
    
def pathfind_origo(point):
    global cubes
    global outside
    global inside
    visited = set()
    pq = PriorityQueue()
    (x,y,z) = point
    pq.put((x^2+y^2+z^2,point))

    while not pq.empty():
        point = pq.get()[1]
        visited.add(point) 

        if point in outside:
            outside.update(visited)
            return True
        
        if point in inside:
            inside.update(visited)
            return False
        x,y,z = point
        for neighbor in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]: # generate neighbor coords
            xn,yn,zn = neighbor
            if (xn,yn,zn) not in cubes and (xn,yn,zn) not in visited:
                pq.put((min([(xn-xo)**2+(yn-yo)**2+(zn-zo)**2 for xo,yo,zo in outside]), (xn,yn,zn))) # check closest point in outside
                visited.add(neighbor)

    inside.update(visited)
    return False
        


main()















