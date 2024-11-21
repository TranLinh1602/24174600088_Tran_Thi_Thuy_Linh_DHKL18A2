#Bài 1: Nhận vào một chuỗi kí tự bất kì. Đếm số kí tự trong chuỗi
#Cách 1
chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
so_ki_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f'Số kí tự trong chuỗi là: {so_ki_tu_trong_chuoi}')
#Cách 2
chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
dem = 0
for chu in chuoi_nhap_vao:
    dem = dem + 1
print(f'số kí tự trong chuỗi là: {dem}')



#Bài 2: Nhập vào một chuỗi bất kì. Xóa các khoảng trống ở đầu và cuối chuỗi
#Cách 1:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
chuoi_sau_khi_xoa = chuoi_nhap_vao.strip()
print(f'Chuỗi sau khi xóa khoảng trong: {chuoi_sau_khi_xoa}')
#Cách 2:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
chuoi_xu_li_dau = ""
kiem_tra_dau = False 
for chu in chuoi_nhap_vao:
    if chu == "" and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_li_dau = chuoi_dao_nguoc_xu_li_dau + chu
chuoi_dao_nguoc = chuoi_xu_li_dau[::-1]
chuoi_dao_nguoc_xu_li_dau = "" 
chuoi_ket_qua = chuoi_dao_nguoc_xu_li_dau[::-1]
print("chuoi sau khi da xoa khoang trong {chuoi_ket_qua}")




#Bài 3: Xóa tất cả các khoảng trống thưaf trong chuỗi
#Vd "         Chuỗi       nhập      vào       " 
#Cách 1:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuỗi nhập vào"
print("chuoi sau khi da xoa khoang trong {chuoi_ket_qua}")
#Cách 2 : Bài tập về nhà, không sử dụng các phương thức


#Dạng 2: áp dụng kết hợp xứ lí vòng lặp và xử lí chuỗi kí tự
#Bài 1: Nhập vào một chuỗi kí tự bất kì, đếm xem có bao nhiêu kí tự là chữ, bao nhiêu kí tự là số và bao nhiêu kí tự đặc biệt
#isalpha(): kiểm tra chữ cái
#isdigit(): kiểm tra số

chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
dem_chu = 0
dem_so = 0
dem_ki_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu += 1
    else:
        if chu.isdigit() == True:
            dem_so += 1
        else:
            dem_ki_tu_dac_biet = dem_ki_tu_dac_biet + 1
print(f'Số chữ cái: {dem_chu}')
print(f'Số số: {dem_so}') 
print(f'Số kí tự đặc biệt: {dem_ki_tu_dac_biet}') 




#BÀi 2: Nhập vào một số bất kì, kiểm tra xem số này có phải số nguyên tố hay không
while True:
    n = input("Nhập vào số nguyên dương cần kiểm tra: ")
    if n.isdigit() == False : 
         print("Giá trị nhập vào không phải giá trị số nguyên dương")
    else:
        break
    
    
#Bài 3: Nhập vào 2 số thực bât kì. Tính tổng 2 số thực đó
while True:
    a = input("Nhập a: ")
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if a.isdigit() == False:
        print("Giá trị nhập vào không phải giá trị số: ")
    else:
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count("-")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("Giá trị nhập vào không phải giá trị số: ")
        else:
            vi_tri_dau_gach = b.find("-")
            if vi_tri_dau_gach != 0:
                print("Giá trị nhập không phải giá trị số")
            else: 
                vi_tri_dau_gach =             
    
    
    
b = input("Nhập vào số thực b: ")
tong = a + b
print(f'Tổng 2 số thực là: {tong}')

    
              
   

                    
    
  
 

  
   
    