file = open('INPUT.txt', 'r')
games = file.readlines()

answer = 0

CUBES_LIMIT = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

for game in games:
    gameId = game.strip().split(':')[0].split(' ')[1]
    sets = game.strip().split(':')[1].split(';')

    is_possible = True

    for cubes_set in sets:
        if not is_possible:
            break

        cubes = list(map(lambda str: str.strip(), cubes_set.split(',')))

        for cube in cubes:
            count = int(cube.split(' ')[0])
            cube_type = cube.split(' ')[1]

            if CUBES_LIMIT[cube_type] < count:
                is_possible = False

                break

    if is_possible:
        answer += int(gameId)

print(answer)
