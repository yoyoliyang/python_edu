# 99乘法表
for x in range(1, 10):
    for y in range(1, x+1):
        print("{} x {} = {}".format(y, x, y*x), end=" ")
    print("\n")
