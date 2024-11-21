#Viết chương trình kiểm tra xem n có phải số nguyên tố hay không
import math
n = int(input("Nhập số cần kiểm tra: "))
if n <= 1:
    print("Hãy nhập một số nguyên dương khác số 1")
else:
    for i in range(2, n + 1):
        if n % i == 0 and n != i:
            print(f'{n} không phải số nguyên tố')
            break
    else:
         print(f'{n} là số nguyên tố')        