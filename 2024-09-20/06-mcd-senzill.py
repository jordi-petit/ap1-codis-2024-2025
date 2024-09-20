# càlcul del màxim comú divisor (algorisme ximplet)

import yogi

a = yogi.read(int)
b = yogi.read(int)
# suposem a,b > 0

if a < b:
    d = a
else:
    d = b

while a % d != 0 or b % d != 0:  # ⇔ not (a % d == 0 and b % d == 0)
    d = d - 1

print(d)
