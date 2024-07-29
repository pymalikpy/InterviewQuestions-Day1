def fibonacci():
    num = 10
    n1, n2 = 0, 1
    print(n1, n2)

    for i in range(2, num):
        sum = n1 + n2

        print(sum)

        n1, n2 = n2, sum
