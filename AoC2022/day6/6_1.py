from collections import deque
with open('input6.txt') as input:
    index = 3
    queue = deque([input.read(1) for i in range(3)],4)

    while True:
        index += 1
        char = input.read(1)
        if not char:
            break

        queue.append(char)

        if len(set(queue)) == 4:
           print(index)
           exit()