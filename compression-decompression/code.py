''' This is a sample input, you can change it of course
    but you have to follow rules of the questions '''

compressed_string = "2a2[3[[c]]2[b]]3a"


def decompress(str=compressed_string):
    string = ""
    number = []
    temp_dig = ""
    multiply = 0
    i = 0
    while i < len(str):
        if str[i] == "[":
            multiply += 1
            if len(temp_dig) > 0:
                number.append(int(temp_dig))
                temp_dig = ""
            else:
                number.append(1)
        elif str[i] == "]":
            if len(number) > 0:
                number.pop()
            multiply -= 1
        else:
            if(str[i].isdigit()):
                temp_dig += str[i]
            else:

                if(multiply > 0 or len(temp_dig) > 0):
                    j = multiply-1
                    Value = 1
                    while j >= 0 and number[j] is not None:
                        Value *= number[j]
                        j -= 1
                    temp = int(temp_dig) if len(temp_dig) > 0 else 1
                    string += (Value*temp)*str[i]
                    temp_dig = ""
                else:
                    string += str[i]

        i += 1
    return string


print(decompress())
