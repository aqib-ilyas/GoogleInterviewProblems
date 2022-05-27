
def find_word_squares(sequence):
    word_length = len(sequence[0])
    word_squares = []
    for word in sequence:
        current_square = []
        current_square.append(word)
        dump = {}

        i = 1
        while i < word_length:
            found = False
            prefix = ""
            for s in current_square:
                prefix += s[i:i+1]
            for j in range(len(sequence)):
                if word != sequence[j] and dump.get(sequence[j], None) is None:
                    if prefix == sequence.__getitem__(j)[0:i]:
                        found = True
                        current_square.append(sequence[j])
                        break
            if(not found and len(current_square) > 1):
                i = i - 2
                dump[current_square.pop()] = 1
            i += 1

        if len(current_square) > 0:
            if len(current_square) == len(current_square[0]):
                word_squares.append(current_square)
    return word_squares


if __name__ == '__main__':
    INPUT = ["BALL", "ABLE", "AREA", "DEAR", "LEAD", "YARD", "LADY"]
    print(find_word_squares(INPUT))
