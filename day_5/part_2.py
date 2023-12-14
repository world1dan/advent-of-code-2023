file = open('INPUT.txt', 'r')
lines = file.readlines()


seeds = list(map(lambda s: int(s.strip()), lines[0].split(': ')[1].split(' ')))
print(seeds)
maps = []

i = 2




while i < len(lines):
    buf = []

    while i < len(lines):
        if lines[i] == '\n':
            i += 1

            break
        
        if not ':' in lines[i]:
            buf.append(lines[i].strip())
        
        i += 1

    maps.append(buf)
    


test = [
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4'
]


def convert(source_num, destination_map):
    for row in destination_map:
        d_r_start = int(row.split()[0])
        s_r_start = int(row.split()[1])
        r_len = int(row.split()[2])

        source_range = range(s_r_start, s_r_start + r_len)

        if not source_num in source_range: continue

        offset = source_num - s_r_start

        destination_num = d_r_start + offset

        return destination_num

    return source_num


def process_seed(seed_num):
    for m in maps:
        seed_num = convert(seed_num, m)

    return seed_num


lowest = 0

for seed in seeds:
    location = process_seed(seed)

    if location < lowest or lowest == 0:
        lowest = location

print(lowest)
