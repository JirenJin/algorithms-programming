i = 0
p = 1
while p > 1/100.0:
    p *= (365 - i) / 365.0
    i += 1
print i, p
