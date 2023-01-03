# If we can find a repeating pattern we can just run algo for one such cycle and then mult by 1 trillion/cycle. 
# Tried to just print the differece in the highest point each input-cycle, and it turns out 
# the first one is weird but afterwards it repeats each cycle!                                                       newline

highest_points = [0]
rocks_per_input_cycle = [0]

def main():
    global highest_points
    global rocks_per_input_cycle

    drop_rocks(6000)

    #for idx in range(1,len(highest_points)):
    #    print('highest_points: ',highest_points[idx] - highest_points[idx-1])
    #    print('no_rocks: ',rocks_per_input_cycle[idx] - rocks_per_input_cycle[idx-1] )

    limit = 1_000_000_000_000

    height = 0
    no_of_rocks = 0

    height_diff = highest_points[2] - highest_points[1]
    rocks_diff = rocks_per_input_cycle[2] - rocks_per_input_cycle[1]

    height_first_cycle = highest_points[1] # this is different than all the others. Will be added along with the tail at the end

    
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*1_000_000, height_diff*1_000_000, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*100_000, height_diff*100_000, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*10_000, height_diff*10_000, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*1000, height_diff*1000, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*100, height_diff*100, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff*10, height_diff*10, height_first_cycle, limit)
    height, no_of_rocks = drop_chunk_rocks(height, no_of_rocks, rocks_diff, height_diff, height_first_cycle, limit)

    rocks_left = limit - no_of_rocks
    print(height+drop_rocks(rocks_left))


def drop_chunk_rocks(height, no_of_rocks, rocks_diff, height_diff, height_first_cycle, limit):
    while no_of_rocks + rocks_diff + height_first_cycle < limit:
        height += height_diff
        no_of_rocks += rocks_diff
    return (height, no_of_rocks)


def drop_rocks(no_of_rocks):
    global highest_points
    global rocks_per_input_cycle
    highest_point = 0
    input = open('input17.txt')
    static_rocks = set()

    for rockno in range(no_of_rocks):
        rock = generate_rock(highest_point, rockno % 5)
        falling = True

        while(falling):
            # get input
            char = input.read(1).strip()
            if not char:
                input.seek(0)
                char = input.read(1)
                highest_points.append(highest_point)
                rocks_per_input_cycle.append(rockno)


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
    return highest_point


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

