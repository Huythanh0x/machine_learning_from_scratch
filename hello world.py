set_a = [x*6 +1 for x in range(100)]
set_b = [x*6 -1 for x in range(100)]
mylist = (set_a+set_b)
mylist.sort()
print(mylist)
mylist_stk = []
from math import sqrt

count = 1
i = 1
while count < 110:
    i += 2
    for k in range(2, 1+int(sqrt(i+1))):
        if i%k == 0:       
            break
    else:
        mylist_stk.append(i)
for x in mylist:
    if x in mylist_stk:
        mylist.remove(x)
print(mylist)
print(mylist_stk)