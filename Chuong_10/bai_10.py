# Viết chương trình nhập vào một chuỗi ký tự, trả về kết quả chuỗi mới sau khi dồn tất cả số sang bên trái
chuoi_nhap_vao = input("Nhap chuoi can kiem tra: ")
so = ""
chu = ""
for i in chuoi_nhap_vao:
    if i.isdigit():
        so += i
    else:
        chu += i
print(f"Ket qua la: {so}{chu}")        
    
   