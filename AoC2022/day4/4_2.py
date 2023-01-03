with open('input4.txt') as input:
    counter = 0

    for line in input:
        elf1, elf2 = line.strip().split(',')
        elf1_start, elf1_stop = elf1.split('-')
        elf2_start, elf2_stop = elf2.split('-')
        if not((int(elf1_start) > int(elf2_stop)) or (int(elf2_start) > int(elf1_stop))):
            counter +=1
        
    print(counter)