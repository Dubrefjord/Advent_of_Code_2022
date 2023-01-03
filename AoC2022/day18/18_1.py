
cubes = set()
sides = 0
# parse data, create cubes
for line in open('input18.txt').readlines():
    line = line.strip().split(',')
    cubes.add((int(line[0]),int(line[1]),int(line[2])))

for x,y,z in cubes:
    if (x-1,y,z) not in cubes:
        sides +=1
    if (x+1,y,z) not in cubes:
        sides +=1
    if (x,y-1,z) not in cubes:
        sides +=1
    if (x,y+1,z) not in cubes:
        sides +=1
    if (x,y,z-1) not in cubes:
        sides +=1
    if (x,y,z+1) not in cubes:
        sides +=1

print(sides)
    
