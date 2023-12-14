file = open('INPUT.txt', 'r')
lines = file.readlines()

t = int(lines[0].split(':')[1].strip().replace(' ', ''))
d = int(lines[1].split(':')[1].strip().replace(' ', ''))



hold_mill = 0
ways = 0


while hold_mill <= t:
    rem_time = t - hold_mill
    hold_mill += 1

    if rem_time * hold_mill > d:
        ways += 1



print(ways)
