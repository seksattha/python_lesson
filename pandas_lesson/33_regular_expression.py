import re

#

def search_demo():
    pattern = re.compile(r'\w\d')
    content = ('E5 : error')
    if pattern.search(content):
        print('found number this pattern')
    else:
        print("not found")

if __name__ == '__main__':
    search_demo()