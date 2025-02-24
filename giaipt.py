# ####################Tính phương trình bậc 2#####################
from math import sqrt

print("Giải phương trình bậc 2: ax^2+bx+c=0")
a= int(input("Nhập a = "))
b= int(input("Nhập b = "))
c= int(input("Nhập c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else :
            print("Phương trình vô nghiệm")
    else :
        if c == 0:
            print("Phương trình có nghiệm x=0")
        else :
            x = -b/c
            print(f"Phương trình có nghiệm x={x}")

else :
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print(f"Phương trình có nghiệm kép x={x}")
    else :
        x1 = float((-b + sqrt(delta))/(2*a))
        x2 = float((-b - sqrt(delta))/(2*a))
        print("Phương trình có hai nghiệm phân biệt")
        print (f"x1={x1}")
        print (f"x2={x2}")