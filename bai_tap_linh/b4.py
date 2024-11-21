#Viết chương trình hiển thị các số nguyên tố từ a đến b
import math
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a < 0 or b < 0:
    print("Hãy nhập một số khác")
elif a > b:
    print("Số này không chấp nhận") 
else:
    for k in range(a, b + 1): 
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0 :
                break
        else:
            print(f' Số nguyên tố trong khoảng từ {a} đến {b} là {k}')