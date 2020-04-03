def NumberOf1(n):
    count = 0
    while (n):
        count += 1
        n = (n - 1) & n
    return count


print(NumberOf1(16))
