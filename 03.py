def fabonacci(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        yield a
        a, b = b, a+b
        i += 1


for temp in fabonacci(10):
    print(temp)
