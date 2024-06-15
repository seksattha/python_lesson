#ทีนี้ดูเหมือนว่าจะไม่มีปัญหาอะไร แต่ความจริงแล้วมันมีปัญหาอยู่
# ถ้ามีการตั้งชื่อ Method ที่เหมือนในแต่ละ Class มันจะไปเอาอันที่อยู่ด้านบนมาก่อน
# ในกรณีนี้จะสร้าง method ชื่อว่า ฺฺBrowse ขึ้นมาทั้งใน Class camera และ media player
# พอสร้างแบบนี้ขึ้นมา มันจะไปรันใน Class camera แทน เพราะว่ามันจะเจอกัน
class Camera:
    def take_photo(self):
        print("Taking photo")
    def delete_photo(self):
        print("Delete photo")
    def browse(self):
        print("Browse photo album")
class Phone:
    def call(self,number):
        print("Calling: {}".format(number))
    def send_SMS(self,number, Text):
        print("Sending to {} with {}".format(number,Text))

class Mediaplayer:
    def playSong(self):
        print("playing a song")
    def browse(self):
        print("browse media library")

class Smartphone(Camera,Phone, Mediaplayer): #A Combination of ability from Phone class and Camera class
    def __init__(self,brand, model):
        self.model = model
        self.brand = brand
    def share(self):
        print("Share something")

if __name__ == '__main__':
    s = Smartphone("13","Apple")
    s.take_photo()
    s.share()
    s.browse()