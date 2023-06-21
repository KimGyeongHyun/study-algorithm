def eed(a, b):

    if b == 0:
        # print(a, b, 1, 0)
        return a, 1, 0
    
    g, x, y = eed(b, a%b)
    # print(a, b, x, y)
    return g, y, x - y * (a // b)

print(eed(550, 330))