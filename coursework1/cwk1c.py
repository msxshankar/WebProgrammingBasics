# Highest count items

def count_occurences(input_string):
    input_string = input_string.split(', ')
    print(input_string)
    x = 0
    y = 0
    count_array = []
    number_array = []
    position = []
    returned_list = []
    count = 0
    for i in range(0, len(input_string)-1):
        if len(input_string) == 0:
            for i, x in enumerate(count_array):
                if x == max(count_array):
                    position.append(i)
            max_value = max(count_array)
            for k in position:
                returned_list.append([number_array[k], max_value])
            return returned_list
            break
        for j in range(0, len(input_string)-1):
            if input_string[x] == input_string[y+1]:
                count += 1
                y += 1
            else:
                y += 1
        x = 0
        y = 0
        count_array.append(count+1)
        number_array.append(input_string[x])
        count = 0
        first = input_string[x]
        for k in input_string[:]:
            if k == first:
                input_string.remove(k)
