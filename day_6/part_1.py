file = open('INPUT.txt', 'r')
lines = file.readlines()

time = list(map(lambda n: int(n), lines[0].split(':')[1].strip().split()))
distance = list(map(lambda n: int(n), lines[1].split(':')[1].strip().split()))


race_i = 0

answer = 0


for race_i in range(len(time)):
    t = time[race_i]
    d = distance[race_i]

    hold_mill = 0

    ways = 0


    while hold_mill <= t:
        rem_time = t - hold_mill

        total_d = rem_time * hold_mill

        hold_mill += 1

        if total_d > d:
            ways += 1
    
    
    print(race_i + 1, ways)


    if ways != 0:
        if answer == 0:
            answer = ways

            continue

        answer = answer * ways


print(answer)
