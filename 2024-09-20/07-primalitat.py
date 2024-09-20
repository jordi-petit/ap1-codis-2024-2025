# solució Pelayo S.

import yogi

n = yogi.read(int)

if n <= 1:
    print("No és primer")
else:
    d = 0  # número de divisores de n
    i = 1
    while i * i <= n and d < 2:
        if n % i == 0:
            d = d + 1
        i = i + 1

    if d < 2:
        print("Primer")
    else:
        print("Compost")
