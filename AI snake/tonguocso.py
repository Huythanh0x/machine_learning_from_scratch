given_number = input().split(" ")
given_number = int(given_number)
def sum_of_common_dev(given_number):
    sum = 0
    for i in range(1,given_number):
        if given_number % i == 0:
            sum += i
    return sum

print(sum_of_common_dev(given_number))    