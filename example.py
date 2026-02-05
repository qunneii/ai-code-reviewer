def bad_function():
    x = 10
    y = 20  # unused

    for i in range(3):
        if i > 1:
            for j in range(3):
                if j > 0:
                    print(i, j)

    return x
