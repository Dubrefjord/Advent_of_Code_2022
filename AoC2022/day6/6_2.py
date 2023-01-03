from collections import deque
with open('input6.txt') as input:
    index = 13
    queue = deque([input.read(1) for i in range(13)],14)

    while True:
        index += 1
        char = input.read(1)
        if not char:
            break

        queue.append(char)
    
        if len(set(queue)) == 14:
           print(index)
           exit()