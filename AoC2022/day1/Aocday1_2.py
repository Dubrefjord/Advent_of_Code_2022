first_max = 0
second_max = 0
third_max = 0
current_carry = 0
with open("input.txt") as input:
    for line in input:
        if line.startswith('\n'): #current_carry now holds the total cals carried by one elf
            if current_carry > third_max:
                third_max = current_carry
            if third_max > second_max:
                #swapping third and second
                third_max,second_max = second_max,third_max 
            if second_max > first_max:
                #swapping second and first
                second_max,first_max = first_max,second_max 
            current_carry = 0
            continue
        current_carry += int(line)
print(first_max + second_max + third_max)
