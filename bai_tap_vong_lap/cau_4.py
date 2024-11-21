n = int(input("Nhap so nguyen duong n: "))
if n < 1:
    print("So nay khong phai so nguyen to")
else:    
    k = n 
    for i in range(n):
        if n % k == 0 and k != n and k != 1 :
            print("So nay khong phai la so nguyen to")
            break
        k = k - 1
    else: 
        print("So nay la so nguyen to")    