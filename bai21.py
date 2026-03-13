chuan = float(input("Nhap diem chuan: "))

d1, d2, d3 = map(float, input("Nhap 3 mon: ").split())
khuvuc = input("Nhap khu vuc (A,B,C,X): ")
doituong = int(input("Nhap doi tuong (1,2,3,0): "))

kv = 0
if khuvuc == "A":
    kv = 2
elif khuvuc == "B":
    kv = 1
elif khuvuc == "C":
    kv = 0.5

dt = 0
if doituong == 1:
    dt = 2.5
elif doituong == 2:
    dt = 1.5
elif doituong == 3:
    dt = 1

tong = d1 + d2 + d3 + kv + dt

if d1 == 0 or d2 == 0 or d3 == 0:
    print("Rot")
elif tong >= chuan:
    print("Dau")
else:
    print("Rot")

print("Tong diem:", tong)
