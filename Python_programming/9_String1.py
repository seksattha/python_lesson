r = "Dream"
t = "Theater"
print(r)
print(t)
print(r+t)
s = r  + t #concatenate
print(s)
line = ">>" * 40
print(line)
s = "0915679821"
print(s[0:5])
print(s[0::2])
print(s[-1:])


s = "Seksatta Bang-Aw"
for i in range(len(s)):
    print("{:>3}".format(i), end="")
print()
for i in range(-len(s),0,1):
    print("{:>3}".format(i), end="")
print()
for i in range(len(s)):
    print("{:>3}".format(s[i]), end ="")
print()

