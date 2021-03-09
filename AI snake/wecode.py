import numpy as np

def is_lucky_number(number):
    count = 0
    for i in number: 
        if i=="4" or i == "7":
            count += 1       
    if count == 4 or count == 7:
        return True
    else:
        return False

given_number = input().split()
given_number = str(given_number[0])
if is_lucky_number(given_number):
    print("YES")
else:
    print("NO")

    
    