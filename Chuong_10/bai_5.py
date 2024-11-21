#Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
chuoi_nhap_vao = input("Nhập chuỗi cần kiểm tra: ")
chu_viet_hoa = 0
chu_viet_thuong = 0
for i in chuoi_nhap_vao:
    if i.isupper() == True:
        chu_viet_hoa = chu_viet_hoa + 1
    else:
        if i.islower() == True:
            chu_viet_thuong = chu_viet_thuong + 1
print(f'Chữ viết hoa là: {chu_viet_hoa}')            
print(f'Chữ viết thường là: {chu_viet_thuong}')
    