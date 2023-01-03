with open('test.txt') as file:
    data = [x.strip() for x in file.readlines()]
    x=0
    y=0
   
    print(data[y][x])
    #print([row[x] for row in data[y+1:]]) # south
    #print([row[x] for row in data[y-1::-1] if y-1 >= 0]) # north
    #print(data[y][:x][::-1]) #west
    #print(data[y][x+1:]) #east
    #print(data[:y-1][x][::-1])

    print([row[x] for row in data[:y][::-1]]) #north
    print([row[x] for row in data[y-1::-1] if y-1 >= 0]) # north
    
    #print([row[x] for row in data[y:][::-1] if y-1 >= 0]) # north
    #print(data[y])
    #print(data[y][:])
    
    #print(data[y][4:0:-1])
    #
    

    #print(data[y-1::-1][x])
    #print(data[y+1][x])
    #print(data[y][x+1::-1])
    #print(data[y][x+1:])