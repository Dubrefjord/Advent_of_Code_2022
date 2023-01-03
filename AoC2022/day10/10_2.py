pixels, x_value = '', 1

for line in open('input10.txt'):
    line = line.strip().split()
    if line[0] == 'noop':
        pixels += '#' if len(pixels)%40 in range(x_value-1,x_value+2) else '.'
    if line[0] == 'addx':
        pixels += '#' if len(pixels)%40 in range(x_value-1,x_value+2) else '.'
        pixels += '#' if len(pixels)%40 in range(x_value-1,x_value+2) else '.'
        x_value += int(line[1])

for i in range(0, len(pixels), 40):
    print(pixels[i:i+40])