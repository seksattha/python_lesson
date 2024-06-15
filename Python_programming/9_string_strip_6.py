def demo():
    s = "Thailand"
    t = "Thailand  "
    print(s==t)

    u = t.strip()
    print(s==u)

def demo_isdigit():
    plate = "1กท4567"
    total = 0
    for i in plate:
        if i.isdigit():
           total += int(i)

    return total
# demo()

def remove_nonDigit(s):
    output = ""
    for t in s:
        if t.isdigit():
            output = output + t
    return output,type(output)

print(demo_isdigit())
print(remove_nonDigit("4444-23434-55664-23434"))
print(remove_nonDigit("085-123-4567"))