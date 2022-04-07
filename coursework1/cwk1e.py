# Word Search

def wordsearch(search_string):

    puzzle = [['R', 'U', 'N', 'A', 'R', 'O', 'U', 'N', 'D', 'D', 'L'],
              ['E', 'D', 'C', 'I', 'T', 'O', 'A', 'H', 'C', 'Y', 'V'],
              ['Z', 'Y', 'U', 'W', 'S', 'W', 'E', 'D', 'Z', 'Y', 'A'],
              ['A', 'K', 'O', 'T', 'C', 'O', 'N', 'V', 'O', 'Y', 'V'],
              ['L', 'S', 'B', 'O', 'S', 'E', 'V', 'R', 'U', 'C', 'I'],
              ['B', 'O', 'B', 'L', 'L', 'C', 'G', 'L', 'P', 'B', 'D'],
              ['L', 'K', 'T', 'E', 'E', 'N', 'A', 'G', 'E', 'D', 'L'],
              ['I', 'S', 'T', 'R', 'E', 'W', 'Z', 'L', 'C', 'G', 'Y'],
              ['A', 'U', 'R', 'A', 'P', 'L', 'E', 'B', 'A', 'Y', 'G'],
              ['R', 'D', 'A', 'T', 'Y', 'T', 'B', 'I', 'W', 'R', 'A'],
              ['T', 'E', 'Y', 'E', 'M', 'R', 'O', 'F', 'I', 'N', 'U']]

    y = 0
    x = 0
    v = 0
    rotate = 0
    listcount = 0
    next = 0
    down = 0
    condition = True
    firstletter_array = []
    search_string_array = []
    tuplelist = []
    y_position = []
    x_position = []
    search_string = search_string.upper()
    for char in search_string:
        search_string_array.append(char)
    while condition is True:
        if y > 10 or x > 10 or y < 0 or x < 0:
            y = down
            x = next
            rotate += 1
            firstletter_array = []
            y_position = []
            x_position = []

        elif (y > 10 or x > 10 or y < 0 or x < 0) and rotate == 7:
            if next == 11:
                down += 1
                y = down
                next = 0
                x = next
                rotate = 0
                firstletter_array = []
                y_position = []
                x_position = []
            else:
                y = down
                x = next
                firstletter_array = []
        else:
            y_position.append(y)
            x_position.append(x)
            try:
                firstletter_array.append(puzzle[y][x])
            except IndexError:
                if rotate == 7:
                    next += 1
                    x = next
                    rotate == 0
                    firstletter_array = [search_string_array]
                else:
                    firstletter_array = [search_string[0]]
                    rotate += 1
            if firstletter_array == search_string_array:
                condition = False
                for i, x in enumerate(firstletter_array):
                    if x == firstletter_array[listcount]:
                        if rotate == 2:
                            tuplelist.append(tuple([y_position[v], 0]))
                        else:
                            tuplelist.append(tuple([y_position[v], i]))
                        listcount += 1
                        v += 1
                return tuplelist

            else:
                if rotate == 0:
                    x += 1
                elif rotate == 1:
                    y += 1
                    x += 1
                elif rotate == 2:
                    y += 1
                elif rotate == 3:
                    x -= 1
                    y += 1
                elif rotate == 4:
                    x -= 1
                elif rotate == 5:
                    y -= 1
                    x -= 1
                elif rotate == 6:
                    y -= 1
                elif rotate == 7:
                    y -= 1
                    x += 1
                else:
                    condition = False
                    return "Not found!"
