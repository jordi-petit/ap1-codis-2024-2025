# llegeix una hora i li suma un segon

h = int(input())
m = int(input())
s = int(input())
print(h, m, s)

s = s + 1
if s == 60:
    s = 0
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0

print(h, m, s)
