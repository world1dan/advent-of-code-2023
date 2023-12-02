file = open('INPUT.txt', 'r')
games = file.readlines()

answer = 0

for game in games:
    sets = game.strip().split(':')[1].split(';')

    cubes_min = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for cubes_set in sets:
        cubes = list(map(lambda str: str.strip(), cubes_set.split(',')))

        for cube in cubes:
            count = int(cube.split(' ')[0])
            cube_type = cube.split(' ')[1]

            cubes_min[cube_type] = max(cubes_min[cube_type], count)

    set_power = 1 

    for key in cubes_min:
        set_power *= cubes_min[key]

    answer += int(set_power)

print(answer)
