# set of coords. For future work: figure out when we can remove coords.                                                           newline
def main():
    highest_point = 0
    input = open('input17.txt')
    static_rocks = set()

    for rockno in range(2022):
        rock = generate_rock(highest_point, rockno % 5)
        falling = True

        while(falling):
            # get input
            char = input.read(1).strip()
            if not char:
                input.seek(0)
                char = input.read(1)

            # check if sideways move => collision
            sideways = True
            moved_rock = [(x+1,y) for x,y in rock] if char == '>' else [(x-1,y) for x,y in rock]

            for x,y in moved_rock:
                if x > 7 or x < 1 or (x,y) in static_rocks:
                    sideways = False
                    break

            # move sideways unless collision
            rock = moved_rock[:] if sideways else rock

            # check move down => collision. If collision, add rock to static_rocks and break
            moved_rock = [(x,y-1) for x,y in rock]

            for x,y in moved_rock:
                if y < 1 or (x,y) in static_rocks:
                    falling = False
                    static_rocks.update(rock)
                    highest_point = max([highest_point, max([y for _,y in rock])])
                    break

            # move down unless collision
            rock = moved_rock[:] if falling else rock
    
    print(highest_point)


def generate_rock(highest_point, rock_number):
    match rock_number:
        case 0:
            return [(3,highest_point+4),(4,highest_point+4),(5, highest_point+4),(6,highest_point+4)]
        case 1:
            return [(3, highest_point+5),(4, highest_point+5),(5, highest_point+5),(4, highest_point+4),(4,highest_point+6)]
        case 2:
            return [(3, highest_point+4),(4, highest_point+4),(5, highest_point+4),(5, highest_point+5),(5, highest_point+6)]
        case 3: 
            return [(3, highest_point+4),(3,highest_point+5),(3,highest_point+6),(3,highest_point+7)]
        case 4:
            return [(3, highest_point+4),(4,highest_point+4),(3,highest_point+5),(4,highest_point+5)]
        case _:
            raise Exception('rock_number must be between 0-4 (mod 5). Received ', rock_number)






main()

