point_dict = {}

def main():
    fill_dictionary()
    tot_points = 0
    with open('input2.txt') as input:
        for line in input:
            tot_points += point_dict[line.strip()]
    print(tot_points)

def fill_dictionary():
    possible_outcomes = ['A X', 'A Y', 'A Z', 'B X', 'B Y', 'B Z', 'C X', 'C Y', 'C Z']
    for outcome in possible_outcomes:
        points = 0
        opponent_move = outcome[0]
        result = outcome[2]
        my_move = ''
        
        if(result == 'X'):
            my_move = chr(ord('A')+((ord(opponent_move)-ord('A')-1) % 3))
        if(result == 'Y'):
            points += 3
            my_move = opponent_move
        if(result == 'Z'):
            points += 6
            my_move = chr(ord('A')+((ord(opponent_move)-ord('A')+1) % 3))
            
        points += ord(my_move)-ord('A')+1
        point_dict[outcome] = points



if __name__ == "__main__":
    main()