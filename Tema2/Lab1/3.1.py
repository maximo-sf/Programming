for num in range(1, 51):
    if num > 20 and num % 17 == 0:
        break
    if num % 3 == 0:
        continue
    print(num)
