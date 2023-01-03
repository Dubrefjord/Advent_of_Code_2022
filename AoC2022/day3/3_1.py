
def main():
    with open('input3.txt') as file:
        collisions=[]
        for line in file:
            first_half,second_half = split_string(line.strip())
            letters_in_first = {}
            for char in first_half:
                letters_in_first[char] = 1
            for char in second_half:
                if letters_in_first.get(char,0) > 0: 
                    collisions.append(char)
                    break
        
        sum_priority=0
        for char in collisions:
            sum_priority += calc_priority(char)
        
        print(sum_priority)

            
def split_string(string):
    length = len(string)
    return string[0:length//2],string[length//2:]

def calc_priority(char):
    if char.isupper():
        return ord(char)-ord('A')+27
    if char.islower():
        return ord(char)-ord('a')+1

if __name__ == "__main__":
    main()