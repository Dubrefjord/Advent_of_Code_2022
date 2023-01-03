class Tree:
    def __init__(self,height):
        self.height = height
        self.visible = False

with open('input8.txt') as input:
    width = len(input.readline().strip())
    input.seek(0)
    visible_trees = 0
    highest_north = [ -1 for i in range(width)]
    highest_south = [[] for i in range(width)]

    for line in input:
        line = line.strip()
        highest_west = -1
        highest_east = []
        for idx, height in enumerate(line):
            tree = Tree(int(height))
            
            if tree.height > highest_west:
                highest_west = tree.height
                tree.visible = True
            
            if tree.height > highest_north[idx]:
                highest_north[idx] = tree.height
                tree.visible = True

            highest_east = [x for x in highest_east if x.height > tree.height]        
            highest_east.append(tree)

            highest_south[idx] = [x for x in highest_south[idx] if x.height > tree.height]
            highest_south[idx].append(tree)

            if tree.visible:
                visible_trees += 1

        for tree in highest_east:
            if not tree.visible:
                tree.visible = True
                visible_trees += 1
    for treelist in highest_south:
        for tree in treelist:
            if not tree.visible:
                tree.visible = True
                visible_trees += 1
    print(visible_trees)

        

             
            
