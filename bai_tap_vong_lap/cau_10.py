#Viết chương trình in ra tổng số nguyên từ một tới n
n = int(input("Nhập số n: "))
tong = 0
for i in range(1,n+1):
    tong += i 
print(f'{tong}')       
    