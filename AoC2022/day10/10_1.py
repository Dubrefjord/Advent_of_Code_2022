x_cycles, x_value, sum = [1], 1, 0

for line in open('input10.txt'):
    line = line.strip().split()
    if line[0] == 'noop':
        x_cycles.append(x_value)
    if line[0] == 'addx':
        x_cycles.append(x_value)
        x_cycles.append(x_value)
        x_value += int(line[1])
for i in range(20, len(x_cycles), 40):
    sum += i*x_cycles[i]
print(sum)
