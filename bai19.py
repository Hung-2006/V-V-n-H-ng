h1, m1, s1 = map(int, input("Nhap gio phut giay [1]: ").split())
h2, m2, s2 = map(int, input("Nhap gio phut giay [2]: ").split())

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

hieu = abs(t2 - t1)

gio = hieu // 3600
phut = (hieu % 3600) // 60
giay = hieu % 60

print("Hieu thoi gian:", gio, "gio", phut, "phut", giay, "giay")
