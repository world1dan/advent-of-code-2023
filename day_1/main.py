file = open('INPUT.txt', 'r')
words = file.readlines()
answer = 0

d_words = [
    'one', 
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

for word in words: 
    first_d = 0
    last_d = 0

    i = 0

    while first_d == 0:
        char = word[i]

        # Check if the character is a digit
        if char.isdigit():
            first_d = char
            break

        # Check if the substring from the current position matches any digit word
        for digit_w_index in range(len(d_words)):
            digit_w = d_words[digit_w_index]

            for j in range(len(digit_w)):
                # Break the loop if characters don't match
                if word[i + j] != digit_w[j]:
                    break

                if j == len(digit_w) - 1:
                    first_d = digit_w_index + 1

        i += 1

    i = 0

    # Loop to find the last digit in the word (searching in reverse)
    while last_d == 0:
        char = word[::-1][i]

        if char.isdigit():
            last_d = char
            break

        # Check if the reversed substring from the current position matches any reversed digit word
        for digit_w_index in range(len(d_words)):
            digit_w = d_words[digit_w_index][::-1]

            for j in range(len(digit_w)):
                if word[::-1][i + j] != digit_w[j]:
                    break

                if j == len(digit_w) - 1:
                    last_d = digit_w_index + 1

        i += 1

    answer += int(str(first_d) + str(last_d)) 

print(answer)
