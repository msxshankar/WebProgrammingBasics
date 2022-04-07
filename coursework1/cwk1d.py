# Game of Life

def gameoflife(x_cycle):

    origin = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    new_origin = origin.copy()
    check_array = []
    a = 0
    b = 0
    count = 0
    condition = True

    while condition is True:
        count += 1
        if count == x_cycle:
            condition is False
            return new_origin
        else:
            check_array.append(origin[a][b+1])
            check_array.append(origin[a+1][b+1])
            check_array.append(origin[a+1][b])
            check_array.append(origin[a+1][b-1])
            check_array.append(origin[a][b-1])
            check_array.append(origin[a-1][b-1])
            check_array.append(origin[a-1][b])
            check_array.append(origin[a-1][b+1])
            total = sum(check_array)
            if origin[a][b] == 0:
                if total == 3:
                    origin[a][b] == 1
                    new_origin.pop([a][b])
                    new_origin.insert([a][1], a)
                else:
                    origin[a][b] == 0
                    new_origin.pop([a][b])
                    new_origin.insert([a][b], a)
            if origin[a][b] == 1:
                if total == 2 or total == 3:
                    origin[a][b] == 1
                    new_origin.pop([a][b])
                    new_origin.insert([a][b], a)
                else:
                    origin[a][b] == 0
                    new_origin.pop([a][b])
                    new_origin.insert([a][1], a)
            a += 1
            b += 1
