def main():
    with open('input9.txt') as input:
        knot_position = [[0,0] for i in range(10)]
        visited = {(0,0)}
        for line in input:
            line = line.strip().split()
            for i in range(int(line[1])):
                if line[0] == 'R':
                    knot_position[0][1] += 1
                if line[0] == 'L':
                    knot_position[0][1] -= 1
                if line[0] == 'U':
                    knot_position[0][0] += 1
                if line[0] == 'D':
                    knot_position[0][0] -= 1
                for idx,knot in enumerate(knot_position):
                    if idx == 0:
                        continue
                    if not is_touching(knot_position[idx-1],knot_position[idx]):
                        move_tail(knot_position[idx-1],knot_position[idx])
                        if idx == 9:
                            visited.add(tuple(knot))
        print(len(visited))

def is_touching(head,tail):
    return True if abs(head[0]-tail[0])<=1 and abs(head[1]-tail[1])<=1 else False

def move_tail(head,tail):
    if head[0] == tail[0]:
        tail[1] += (head[1]-tail[1])//abs(head[1]-tail[1]) 

    elif head[1] == tail[1]:
        tail[0] += (head[0]-tail[0])//abs(head[0]-tail[0])
    else:
        tail[1] += (head[1]-tail[1])//abs(head[1]-tail[1])
        tail[0] += (head[0]-tail[0])//abs(head[0]-tail[0])
    return
        
    


if __name__ == "__main__":
    main()