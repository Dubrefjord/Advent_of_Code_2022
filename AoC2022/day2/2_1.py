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
        my_move = outcome[2]
        if(my_move == 'X'):
            points += 1
            if(opponent_move == 'A'):
                points += 3
            if(opponent_move == 'C'):
                points += 6
        if(my_move == 'Y'):
            points += 2
            if(opponent_move == 'B'):
                points += 3
            if(opponent_move == 'A'):
                points += 6
        if(my_move == 'Z'):
            points += 3
            if(opponent_move == 'C'):
                points += 3
            if (opponent_move == 'B'):
                points += 6
        point_dict[outcome] = points



if __name__ == "__main__":
    main()