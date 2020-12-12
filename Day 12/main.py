f = open('text.txt', 'r')

arr = [[i[0], i[1:]] for i in f.read().split('\n')]

north_vector = 0
east_vector = 0
angle = 90

for direction, magnitude in arr:
    magnitude = int(magnitude)
    if direction == 'N':
        north_vector += magnitude
    if direction == 'E':
        east_vector += magnitude
    if direction == 'S':
        north_vector -= magnitude
    if direction == 'W':
        east_vector -= magnitude

    if direction == 'R':
        angle += magnitude
        if angle >= 360:
            angle -= 360

    if direction == 'L':
        angle -= magnitude
        if angle < 0:
            angle += 360

    if direction == 'F':
        if angle == 0:
            north_vector += magnitude
        elif angle == 90:
            east_vector += magnitude
        elif angle == 180:
            north_vector -= magnitude
        elif angle == 270:
            east_vector -= magnitude
        else:
            raise Exception('The angle should be one of the above values whereas it is '+str(angle))

print(abs(north_vector)+abs(east_vector))

# Part 2
north_vector = 0
east_vector = 0
waypoint_north_vector = 1
waypoint_east_vector = 10
angle = 90

for direction, magnitude in arr:
    magnitude = int(magnitude)
    if direction == 'N':
        waypoint_north_vector += magnitude
    if direction == 'E':
        waypoint_east_vector += magnitude
    if direction == 'S':
        waypoint_north_vector -= magnitude
    if direction == 'W':
        waypoint_east_vector -= magnitude

    if direction == 'R':
        if magnitude == 90:
            temp = waypoint_north_vector
            waypoint_north_vector = waypoint_east_vector * -1
            waypoint_east_vector = temp
        elif magnitude == 180:
            waypoint_north_vector *= -1
            waypoint_east_vector *= -1
        elif magnitude == 270:
            temp = waypoint_north_vector
            waypoint_north_vector = waypoint_east_vector
            waypoint_east_vector = temp * -1
        else:
            raise Exception('Rotation error')

    if direction == 'L':
        if magnitude == 90:
            temp = waypoint_north_vector
            waypoint_north_vector = waypoint_east_vector
            waypoint_east_vector = temp * -1
        elif magnitude == 180:
            waypoint_north_vector *= -1
            waypoint_east_vector *= -1
        elif magnitude == 270:
            temp = waypoint_north_vector
            waypoint_north_vector = waypoint_east_vector * -1
            waypoint_east_vector = temp
        else:
            raise Exception('Rotation error')

    if direction == 'F':
        north_vector += waypoint_north_vector * magnitude
        east_vector += waypoint_east_vector * magnitude
    print('test')
    print('ok')

print(abs(north_vector)+abs(east_vector))