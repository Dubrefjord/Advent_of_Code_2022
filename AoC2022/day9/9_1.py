def main():
    with open('input9.txt') as input:
        head_position = [0,0]
        tail_position = [0,0]
        visited = {(0,0)}
        for line in input:
            line = line.strip().split()
            for i in range(int(line[1])):
                if line[0] == 'R':
                    head_position[1] += 1
                if line[0] == 'L':
                    head_position[1] -= 1
                if line[0] == 'U':
                    head_position[0] += 1
                if line[0] == 'D':
                    head_position [0] -= 1

                if not is_touching(head_position,tail_position):
                    move_tail(head_position,tail_position)
                    visited.add(tuple(tail_position))
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