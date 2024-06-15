def nato_from_file():
    with open("nato.txt") as f:
        d = {line[0]:line[:-1] for line in f}
        return d

def convert(s):
    d = nato_from_file()
    r = [d[c.upper()] for c in s]
    return "".join(r)

if __name__ == '__main__':
    print(nato_from_file())
    print(convert("Daikin"))