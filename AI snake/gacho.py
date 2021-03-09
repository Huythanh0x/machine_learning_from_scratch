def gacho(con, chan):
    ga = (chan - con*2)/2
    cho = con - ga
    return ga, cho


given_number = input().split()
ga, cho = gacho(int(given_number[0]), int(given_number[1]))
print(int(cho), int(ga))
