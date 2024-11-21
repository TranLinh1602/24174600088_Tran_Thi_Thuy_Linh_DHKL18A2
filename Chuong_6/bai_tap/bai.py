#Tính điểm của sinh viên
diem_chuyen_can = float(input("Nhap diem chuyen can: "))
diem_giua_ki = float(input("Nhap diem giua ki: "))
diem_cuoi_ki = float(input("Nhap diem cuoi ki: "))
if diem_chuyen_can and diem_giua_ki and diem_cuoi_ki > 0:
    diem_trung_binh = (diem_chuyen_can + diem_giua_ki + diem_cuoi_ki)/3
    if diem_trung_binh >= 9:
        print(f"Điểm trung bình của bạn là :{diem_trung_binh}")
        print(f"Loại A")
    elif diem_trung_binh >= 7 and diem_trung_binh < 9:
        print(f"Điểm trung bình của ban là: {diem_trung_binh}")
        print(f"Loại B")
    elif diem_trung_binh >= 5 and diem_trung_binh < 7:
        print(f"Điểm trung bình của bạn là: {diem_trung_binh}")
        print(f"Loại C")
    else:
        print(f"Điểm trung bình của bạn là: {diem_trung_binh}")
        print(f"Loại D")
else:
    print(f"Bạn hãy nhập lại điểm")
            
                         
     