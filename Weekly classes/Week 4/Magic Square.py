"""
In recreational mathematics, a square array of numbers,
usually positive integers, is called a magic square if
the sums of the numbers in each row, each column,
and both main diagonals are the same.

Magic Number = n(n^2+1)/2......n=3,5,7.......

Position of 1 is always in the middle row and last column (n/2,n-1)

Position of 2 == (p-1,q+1)

"""


def magic_square(n):  # n is number of row and column

    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)

    i = n // 2
    j = n - 1

    num = n * n
    count = 1

    while count <= num:
        if i == -1 and j == n:  # Condition 4
            j = n - 2
            i = 0
        else:
            if j == n:  # Column value is exceeded
                j = 0
            if i < 0:  # Row becoming -1
                i = n - 1

        if magicSquare[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[i][j] = count
            count += 1

        i = i - 1
        j = j + 1  # Condition 1

    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()

    print("Th sum of each row/column/diagonal is: " + str(n * (n ** 2 + 1) / 2))


magic_square(3)

"""



"""
