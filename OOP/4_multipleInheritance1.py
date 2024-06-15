#เป็นการเอาความสามารถในแต่ละ class มารวมกัน
# ในตัวอย่างจะเป็นการนำเอาความสามารถของ กล้อง และ โทรศัพท์มารวมกันเป็น smartphone
class Camera:
    def take_photo(self):
        print("Taking photo")
    def delete_photo(self):
        print("Delete photo")

class Phone:
    def call(self,number):
        print("Calling: {}".format(number))
    def send_SMS(self,number, Text):
        print("Sending to {} with {}".format(number,Text))

class Mediaplayer:
    def playSong(self):
        print("playing a song")
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