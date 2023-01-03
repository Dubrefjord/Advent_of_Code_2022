solid = {}
lowest = 0
grains_of_sand=0

#parse lines add solids, identifiera lägsta punkt
for line in open('input14.txt'):
    line = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.strip().split(' -> ')]
    for idx in range(len(line)-1):
        x1,y1 = line[idx]
        x2,y2 = line[idx+1]
        for i in range(x1,x2+1 if x2>=x1 else x2-1, 1 if x2>=x1 else -1):
            for j in range(y1,y2+1 if y2>=y1 else y2-1, 1 if y2>=y1 else -1):
                solid[(i,j)] = True
                lowest = j if j > lowest else lowest

#while True släng sand, Om sand faller nedanför lägsta solid, break
while True:
    grains_of_sand +=1
    sand = (500,0)
    while True:
        x,y = sand
        if y > lowest: 
            print(grains_of_sand-1)
            exit()
        if not solid.get((x,y+1),False): sand = (x,y+1)
        elif not solid.get((x-1,y+1),False): sand = (x-1,y+1)
        elif not solid.get((x+1,y+1),False): sand = (x+1,y+1)
        else: 
            solid[sand] = True
            break
    