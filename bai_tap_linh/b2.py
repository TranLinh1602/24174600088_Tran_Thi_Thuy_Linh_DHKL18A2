#Viết chương trình kiểm tra xem n có phải số hoàn hảo hay không
n = int(input("Nhập số cần kiểm tra: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương ")
else:
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(f'{n} là số hoàn hảo')
    else:
        print(f'{n} không phải là số hoàn hảo')             