def main():
    with open('input3.txt') as file:
        collisions=[]
        for first_line in file:
            first_line = first_line.strip()
            second_line = next(file).strip()
            third_line = next(file).strip()
            letters_in_first = {}
            letters_in_second = {}
            for char in first_line:
                letters_in_first[char] = 1
            for char in second_line:
                letters_in_second[char] = 1
            for char in third_line:
                if letters_in_first.get(char,0) > 0 and letters_in_second.get(char,0) > 0: 
                   collisions.append(char)
                   break
        
        sum_priority = 0
        for char in collisions:
            sum_priority += calc_priority(char)    
        print(sum_priority)

def calc_priority(char):
    if char.isupper():
        return ord(char)-ord('A')+27
    if char.islower():
        return ord(char)-ord('a')+1

if __name__ == "__main__":
    main()
