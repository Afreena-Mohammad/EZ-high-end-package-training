def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = n // 2, n-1

    while num <= n**2:
        if i == -1 and j == n:
            i, j = 0, n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magic_square[i][j] != 0:
            i, j = i +1, j - 2
            continue
        else:
            magic_square[i][j] = num
            num += 1

        i, j = i -1, j +1 

    return magic_square

def print_magic_square(square):
    for row in square:
        print('\t'.join(map(str, row)))

n = int(input("Enter the size of the magic square (odd number): "))

if n % 2 == 0:
    print("Please enter an odd number.")
else:
    magic_square = generate_magic_square(n)
    print("\nGenerated Magic Square:")
    print_magic_square(magic_square)
