n = int(input("Nhap n: "))

dem = 0
tong = 0

print("Cac uoc so:", end=" ")

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        dem += 1
        tong += i

print("\nCo", dem, "uoc so tong la:", tong)
