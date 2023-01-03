import re

def main():
    no_beacons = {}
    sensors = set()
    beacons = set()
    # parse sensors & beacons
    for line in open('input15.txt'):
        match = re.search(r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)", line)
        match = {item:int(value) for (item,value) in match.groupdict().items()}
        sensor = (match['sx'],match['sy'])
        beacon = (match['bx'],match['by'])
        sensors.add(sensor)
        beacons.add(beacon)
        dist = manhattan_dist(sensor,beacon)
        intervals = get_no_beacon_intervals(sensor,dist).items()
        for y,(new_start,new_end) in intervals:
            if y in no_beacons:
                no_beacons[y].append((new_start,new_end))
            else:
                no_beacons[y] = [(new_start,new_end)]

    for row_number in range(0,4_000_000):
        no_beacons[row_number].extend([(x,row_number) for x,y in sensors.union(beacons) if y == row_number])
        no_beacons[row_number] = eliminate_overlap(no_beacons[row_number]) 
        for _,end in no_beacons[row_number]:
            # if an interval ends in the range, that means the next coordinate is not included in any interval
            if end >= 0 and end <= 4_000_000:
                print(end+1,row_number)
                print((end+1)*4_000_000+row_number)
                exit()       
   

def manhattan_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_no_beacon_intervals(sensor,dist):
    x,y = sensor
    return {y+j:(x-dist+abs(j), x+dist-abs(j)) for j in range(-dist,dist+1)}

def eliminate_overlap(row):
    row.sort()
    new_row = []
    current_start = row[0][0]
    current_end = row[0][1]
    for start,end in row:
        if start <= current_end: 
            current_end = end if end > current_end else current_end
        elif start > current_end:
            new_row.append((current_start,current_end))
            current_start = start
            current_end = end
    new_row.append((current_start,current_end))
    return new_row



if __name__ == "__main__":
    main()






