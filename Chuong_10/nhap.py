chuoi = input("Nhập vào một chuỗi: ")

# Kiểm tra thủ công
if chuoi[:1] == '-' and chuoi[1:]:  # Kiểm tra dấu '-' và chuỗi sau dấu '-'
    so_am = True
    for ky_tu in chuoi[1:]:         # Kiểm tra các ký tự còn lại có phải số
        if ky_tu < '0' or ky_tu > '9':
            so_am = False
            break
print("Số này là số âm")        
