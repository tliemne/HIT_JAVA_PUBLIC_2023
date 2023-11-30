sv={
    'sv1': 1.9,
    'sv2':2.1,
    'sv3':2.4,
    'sv4':2.6,
    'sv5':2.8,
    'sv7':3.0,
    'sv8':3.2,
    'sv9':3.4
}
sosv = sum(2.5 <= diem <= 3.5 for diem in sv.values()) 
print(f"Số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]: {sosv}")
sv_new = 'sv11'
diem1  = 3.6
sv[sv_new] = diem1
sv_can_xoa = [ma_sinh_vien for ma_sinh_vien, diem in sv.items() if diem < 2.0]
for msv in sv_can_xoa:
    del sv[msv]

print("Từ điển sau khi thực hiện các thao tác:")
for msv, diem in sv.items():
    print(f"{msv}: {diem}")