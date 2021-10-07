''' This is a sample input, you can change it of course
    but you have to follow rules of the questions '''

compressed_string = "2[1[b]10[c]]a"


def decompress(str=compressed_string):
    string = ""
    number_stack = []
    replace_index_stack = []
    bracket_index_stack = []
    i = 0
    while i < len(str):
        if str[i] == "[":
            # storing indexes in coressponding stacks
            replace_index_stack.insert(0, i - len(string))
            number_stack.insert(0, int(string))
            bracket_index_stack.insert(0, i+1)
            string = ""
        elif str[i] == "]":
            # updating base string with uncompressed part
            temp = str[bracket_index_stack[0]:i] * number_stack[0]
            str = str.replace(str[replace_index_stack[0]:i+1], temp)
            # updating index to next position from decompressed part
            i = replace_index_stack[0]+len(temp)
            # poping the top item from stacks which is used already
            number_stack.pop(0)
            replace_index_stack.pop(0)
            bracket_index_stack.pop(0)
            string = ""
            continue
        else:
            string += str[i]
        i += 1
    return str


print(decompress())
