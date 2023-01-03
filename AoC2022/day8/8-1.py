with open('input8.txt','r') as input:
    visible_trees = 0
    for row, line in enumerate(input):
        line = line.strip()
        width = len(line)

        for col, char in enumerate(line): 
        
            is_visible = False
            east_west = [int(x) for x in line]
            north_south = [int(x[col]) for x in open('input8.txt','r').readlines()]

            if int(char) > max(east_west[:col-1]):
                visible_trees += 1
                continue

            if int(char) > max(east_west[col+1:]):
                visible_trees += 1
                continue

            if int(char) > max(north_south[:row-1]):
                visible_trees += 1
                continue
            
            if int(char) > max(north_south[row+1:]):
                visible_trees += 1
                continue
    print(visible_trees)
    