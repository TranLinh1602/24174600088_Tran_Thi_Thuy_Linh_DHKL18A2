print("Hello world")

a = "Hello world"
b = "Hello world"

print(a[4])
print(a[::2])
print(a[::])
print(a[::-1])


print(range(5))


for item in a:
    print(item)
    
    
#Hàm đo độ dài kiểu dữ liệu tuần tự: len
print(len(a))
range(len(a)) #Thu được chỉ mục chạy từ 0 đến len(a) - a 
for i in range(len(a)):
    print(a[i])   
    
    
#Tính chất của kiểu dữ liệu chuỗi kí tự
#-Có thể truy cập 
#-Không thể chỉnh sửa
#-Không thể sắp xếp
    

b = "Hello" + "world" 
print(b) 

n = int(input("Nhập vào số nguyên dương: "))
if n > 0:
    print("Đã nhập đúng số nguyên dương")
    
#Các phương thức xử lí chuỗi kí tự
a = "Helloworld123"
#Các phương thức kiểm tra(Trả về cho mình Tri hoặc False)
#Các phương thức này sẽ thường bắt đầu bằng chữ "is"

#-Kiểm tra chuỗi có phải alphanumberic (chỉ có kí tự số và chứ hay không)
print(a.isalnum())  

#-Kiểm tra chuỗi có toàn số hay không (numberic)
a = "1.23"
print(a.isnumeric())

#-Kiểm tra chuỗi có toàn chữ hay không (character)
a = "Hello world"
print(a.isalpha())
#-Kiểm tra chuỗi có nằm trong bảng mã ascii hay không
print(a.isascii())
#-Kiểm tra chuỗi có phải kiểu số hay không
print(a.isdecimal())#số thập phân
print(a.isdigit) #số thông thường



#-Kiểm tra in hoa hay thường
a = "Hello world"
print(a.isupper())

#- Kiểm tra kí tự tồn tại trong chuỗi
print(a.find("llo"))
print(a.count("l"))

#-Phương thức biến đổi (các phương thức này trả về chuỗi kí tự mới, không thay đổi chuỗi kí tự)
a = "Hello world"
#-Xóa kí tự đầu và cuối của chuỗi
a.strip("d")
a.lstrip()
a.rstrip()

#-Thay thế kí tự bất kì
a = "Hello world"
a_sua = a.replace("l","w",2)

#-Biển đổi viết hoa viết thường
a = "Hello world"
a_sua = a.upper() #Hoa
a_sua = a.lower() #thường
a_sua = a.capitalize() #chữ đầu viết hoa

