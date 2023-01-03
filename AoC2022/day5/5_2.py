with open('input5.txt') as input:
    no_of_stacks = len(input.readline())//4
    input.seek(0)
    stacks = [[] for x in range(no_of_stacks)]
    data_collection = True
    
    for line in input:
        if line.startswith(' 1'):
            data_collection = False
            for stack in stacks:
                stack.reverse()
            next(input) # skip newline
            continue
    
        if(data_collection):
            for index in range(0, len(line), 4):
                if not line[index:index+4].isspace():
                    stacks[index//4].append(line[index+1])
        
        if(not data_collection):
            # moving boxes!
            instructions = line.strip().split()
            no_of_boxes = int(instructions[1])
            to_stack = int(instructions[5])-1
            from_stack = int(instructions[3])-1

            stacks[to_stack].extend(stacks[from_stack][-no_of_boxes:])
            stacks[from_stack] = stacks[from_stack][:-no_of_boxes]
            
    print("".join(stack[-1] for stack in stacks))   
       