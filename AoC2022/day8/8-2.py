def check_visibility(height, trees):
    idx = 0
    for tree in trees:
        idx +=1
        if int(tree) >= height:
            break
    return idx

with open('input8.txt') as file:
    data = [x.strip() for x in file.readlines()]
    highest_scenic = 0

    for y,line in enumerate(data):
        for x,char in enumerate(line):
            scenic = check_visibility(int(char), [row[x] for row in data[:y][::-1]])
            scenic *= check_visibility(int(char), [row[x] for row in data[y+1:]])
            scenic *= check_visibility(int(char), data[y][:x][::-1])
            scenic *= check_visibility(int(char), data[y][x+1:])
            highest_scenic = scenic if scenic > highest_scenic else highest_scenic
    
    print(highest_scenic)
