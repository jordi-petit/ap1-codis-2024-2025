a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        m = a
    else:
        m = c
else:
    if b > c:
        m = b
    else:
        m = c

print(m)