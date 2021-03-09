def fibo(n):
    first = 1
    second = 1
    for _ in range(n-2):
        first,second = second,second + first
    return second
number = input()
number = int(number)
if number >= 1 and number <= 30:
    print(fibo(number))
else:
    print("So <x> khong nam trong khoang [1,30]")