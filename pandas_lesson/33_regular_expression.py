import re

#

def search_demo():
    pattern = re.compile(r'\d+')
    content = ('abc 123 def')
    if pattern.search(content):
        print('found number this pattern')
    else:
        print("not found")


def match_demo():
    pattern = re.compile(r'\d+')
    content = ('abc 123 def')
    if pattern.match(content):
        print('found number this pattern')
    else:
        print("not found")

def fullmatch_demo():
    pattern = re.compile(r'\d+')
    content = ('123 def')
    if pattern.fullmatch(content):
        print('found number this pattern')
    else:
        print("not found")


if __name__ == '__main__':
    # search_demo()
    # match_demo()
    # ความแตกต่างที่ชัดเจนระหว่าง search กับ match ก็คือ match จะต้องเจอที่ตัวนำหน้าเลย

    fullmatch_demo()
    # ความแตกต่างที่ชัดเจนระหว่าง search กับ fullmatch ก็คือ search
    # จะหาทั้งหมดถ้าเจอบางส่วนก็ถือว่าเจอ แต่ถ้า full match จะต้องตรงทั้งหมด
    # ในกรณีนี้ก็คือ pattern d+ จะต้องเจอตัวเลข 1 ตัวขึ้นไป แต่พอจะเป็น '123 def' มันจะหาไม่เจอ
