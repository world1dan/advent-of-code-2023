file = open('INPUT.txt', 'r')
lines = file.readlines()

answer = 0

cards = list(map(lambda line: list(map(lambda l: l.strip().split(' '), line.split(':')[1].split('|'))), lines))


def process_card(i):
    global answer 

    answer = answer + 1

    [nums, winning_nums] = cards[i]

    count = 0

    for num in nums:
        if num == '': continue

        if num in winning_nums:
            count += 1

    
    for j in range(i + 1, i + 1 + count):
        process_card(j)


for j in range(len(cards)):
    process_card(j)


print(answer)
