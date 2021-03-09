def is_triangle(a, b, c):
    if(a+b > c) and (b+c > a) and (c+a > b) and a > 0 and b > 0 and c > 0:
        return True
    return False


def count_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    area = round(area, 2)
    area = f'{area:g}'
    return area


def is_right_triangle(a, b, c):
    return a**2 + b**2 == c ** 2 or a**2 == b**2 + c ** 2 or b**2 == c ** 2 + a**2


def is_equilateral(a, b, c):
    return (a == b and b == c) or (a == c and b == c) or (a == b and a == c)


def is_isosceles(a, b, c):
    return a == b and b == c and c == a


a = input()
a = int(a)
b =  input()
b = int(b)
c = input()
c = int(c)
type_triangle = "Tam giac thuong"
if is_right_triangle(a,b,c):
    type_triangle = "Tam giac vuong"
elif is_isosceles(a,b,c):
    type_triangle = "Tam giac deu"
elif is_equilateral(a,b,c):
    type_triangle = "Tam giac can"
    

if is_triangle(a,b,c):
    print(type_triangle + ", dien tich = " + count_triangle(a,b,c))
else:
    print("Khong phai tam giac")
