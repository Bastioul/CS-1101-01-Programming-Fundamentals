def hypotenuse(x, y):
    a = x**2
    b = y**2
    c = a + b
    g = c
    k = 1
    t = 0
    while g >= 1:
        g -= k
        t += 1
        k += 2
        if g <= 1:
            if abs(g) * 2 > k:
                t -= 1
            else:
                pass
            print(g)
            print(k)
            print(f'The dimensions of the triangle are {x}x{y}x{t}')
            print(f'The longest side is {t}.')
            print(f'----------------------------------------------')
            return t