a1 = float(input("Nhập hệ số a1: "))
a2 = float(input("Nhập hệ số a2: "))
b1 = float(input("Nhập hệ số b1: "))
b2 = float(input("Nhập hệ số b2: "))
c1 = float(input("Nhập hệ số c1: "))
c2 = float(input("Nhập hệ số c2: "))
#Ta có hệ phương trình
#a1*x + b1*y = c1
#a2*x + b2*y = c2
#Xét các trường hợp 
#Hệ phương trình có nghiệm duy nhất khi a1/a2 != b1/b2
#Hệ phương trình vô nghiệm khi a1/a2 == b1/b2 != c1/c2
#Hệ phương trình có vô số nghiệm khi a1/a2 == b1/b2 == c1/c2
#Phương pháp giải hệ phương trình bậc nhất 2 ẩn
#Phương pháp thế:
# x = (c1 - b1*y)/a1
# y = (c2*a1 - a2*c1)/(a1*b2 - a2*b1)
#Phương pháp cramer:
#Tính định thức 
A = a1*b2 - a2*b1
if A != 0:
         A1 = b2*c1 - b1*c2
         A2 = a1*c2 - a2*c1
         x = A1/A
         y = A2/A
         print(f'Nghiệm của hệ phương trình là :{x}')
         print(f'Nghiệm của hệ phương trình là :{y}')
else:
    print("Phương pháp Cramer không hỗ trợ tính khi định thức bằng 0")
  
