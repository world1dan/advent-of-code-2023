file = open('INPUT.txt', 'r')
lines = file.readlines()

gears = {}
answer = 0

def isDot(s: str):
    return s == '.'

def isDigit(s: str):
    return s.isdigit()

def isSymbol(s: str, row_i, column_i, num):
    if s == '*':
        existing = gears.get((row_i, column_i), [])
        existing.append(int(num))
        gears.update({(row_i, column_i): existing})

        return True

    return not isDigit(s) and not isDot(s)


for line_i in range(len(lines)):
    line = lines[line_i].strip()

    char_i = 0
    num = ''

    while char_i < len(line):
        if isDigit(line[char_i]):
            num += line[char_i]

            if char_i != len(line) - 1:
                char_i += 1

                continue
            else: 
                char_i += 1


        if num == '':
            char_i += 1

            continue
    
        num_start_i = char_i - len(num)
        num_end_i = char_i

        def checkLeft():
            return num_start_i > 0 and isSymbol(line[num_start_i - 1], line_i, num_start_i - 1, num)

        def checkRight():
            return num_end_i < len(line) - 1 and isSymbol(line[num_end_i], line_i, num_end_i, num)
        
        def checkTop():
            if line_i == 0:
                return False

            top_line = lines[line_i - 1].strip()
            search_start_i = num_start_i - 1 if num_start_i != 0 else num_start_i
            search_end_i = num_end_i + 1 if num_end_i != len(top_line) - 1 else num_end_i
            
            for j in range(len(top_line[search_start_i:search_end_i])):
                char = top_line[search_start_i:search_end_i][j]

                if isSymbol(char, line_i - 1, search_start_i + j, num):
                    return True
            
            return False

        def checkBottom():
            if line_i == len(lines) - 1:
                return False

            bottom_line = lines[line_i + 1].strip()

            search_start_i = num_start_i - 1 if num_start_i != 0 else num_start_i
            search_end_i = num_end_i + 1 if num_end_i != len(bottom_line) - 1 else num_end_i
            
            for j in range(len(bottom_line[search_start_i:search_end_i])):
                char = bottom_line[search_start_i:search_end_i][j]

                if isSymbol(char, line_i + 1, search_start_i + j, num):
                    return True
            
            return False


        if checkLeft() or checkRight() or checkTop() or checkBottom():
            answer += int(num)

        num = ''

        char_i += 1


gears_ratio = 0

for row in gears.values():
    if len(row) != 2:
        continue
    
    gears_ratio = gears_ratio + row[0] * row[1]


print('Part 1 answer:', answer)
print('Part 2 answer:', gears_ratio)
