max = 0
current_carry = 0
with open("input.txt") as input:
    for line in input:
        if line.startswith('\n'): #current_carry now holds the total cals carried by one elf
            if current_carry > max:
                print("found new max! "+str(max))
                max = current_carry
            current_carry = 0
            continue
        current_carry += int(line)
print(max)