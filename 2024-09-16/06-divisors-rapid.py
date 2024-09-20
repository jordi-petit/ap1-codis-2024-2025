import yogi

n = yogi.read(int)

i = 1
while i * i <= n:
    if n % i == 0:
        print(i)
        print(n // i)
    i = i + 1

# millorar la solució per a que no es repeteixin els divisors en cas de quadrats perfectes
# millorar la solució per a que els divisors es mostrin en ordre creixent
