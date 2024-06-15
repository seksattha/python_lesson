def reading_basic():
    with open ("test.txt") as f:
        content = f.read()
    return content
def reading_basic2():
    with open ("test.txt") as f:
        content = f.readline()
    return content
def reading_readline1():
    with open("test.txt") as f:
        for i in f:
            print(i,end="")


def reading_readlines():
    with open("test.txt") as f:
        content = f.readlines()
    return content

def reading_readlines2():
    with open("test.txt") as f:
        content = []
        for line in f.readlines():
            content.append(line.strip())
        return content

def reading_readlines3():
    with open("test.txt") as f:
        content = [line.strip() for line in f.readlines()]
        return content

def reading_non_project_directory():
    with open(r"C:\Users\seksatta\Desktop\test.txt") as f:
        content = f.readlines()
    return content

def reading_unicode():
    with open("test_thai.txt", encoding="utf-8") as f:
        content = f.read()
    return content

def reading_with_newline(filename):
    with open(filename ,"r") as f:
        content = f.readlines()
        content_list = {line.strip().lower() for line in content}
        print(content_list)


def reading_with_newline2(filename):
    with open(filename, "r") as f:
        s = f.read()
        s2 = s.splitlines()
    print(s)
    print("*" * 40)
    print(s2)
    s3 = [i.strip() for i in s2]
    print("*" * 40)
    print(s3)

def reading_with_newline3(filename):
    with open(filename, "r",
              encoding="utf-8") as f:
        s = f.readlines()
        s2 = [i.strip().split(",") for i in s]
        s3 = [i.split(",") for i in s ]
    print(s)
    print("*" * 40)
    print(s2)
    print("*" * 40)
    print(s3)


if __name__ == '__main__':
   filename = "test_read_with_newline_comma"
   reading_with_newline3(filename)


