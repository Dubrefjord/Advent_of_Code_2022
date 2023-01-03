def main():
    with open('input3.txt') as file:
        sum_priority = 0
        for first_line in file:
            first_line = first_line.strip()
            second_line = next(file).strip()
            third_line = next(file).strip()

            for char in third_line:
                if char in first_line and char in second_line: 
                   sum_priority += calc_priority(char)
                   break
        
        print(sum_priority)

def calc_priority(char):
    if char.isupper():
        return ord(char)-ord('A')+27
    if char.islower():
        return ord(char)-ord('a')+1

if __name__ == "__main__":
    main()
