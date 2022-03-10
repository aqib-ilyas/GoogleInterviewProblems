

# Check if every word in the list contains same number of letters
def is_sequence_square(words):
    for word in words:
        if len(words[0]) != len(word):
            return False
    return True

def find_word_squares(sequence):
    word_squares = []
    word_length = len(sequence[0])
    sequence_length = len(sequence)
    possibles = []
    for i in range(sequence_length):
        temp = []
        for index, letter in enumerate(sequence[i]):
            print("INDEX: ", index)
            for j in range(sequence_length):
                if i == j:
                    continue
                if letter == sequence[j][0]:
                    temp.append(sequence[j])
                    print(index, letter, sequence[j][0], sequence[i], temp)
        possibles.append(temp)
    print(possibles)




if __name__ == '__main__':
    INPUT = ["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]
    if(is_sequence_square(INPUT)):
        find_word_squares(INPUT)


