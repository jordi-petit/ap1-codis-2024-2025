import yogi

m = yogi.read(float)
for x in yogi.tokens(float):
    if x > m:
        m = x
print(m)
