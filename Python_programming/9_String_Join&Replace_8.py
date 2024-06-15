import random
def demo_join():
    Station_mrt = ("Hua Lamphong", "Wat Mangkon", "Sam Yan", "Si Lom", "Lumphini", "Khlong Toei", "Queen Sirikit National Convention Centre", "Sukhumvit", "Phetchaburi", "Phra Ram 9", "Thailand Cultural Centre", "Ratchadaphisek", "Lat Phrao", "Phahon Yothin", "Chatuchak Park", "Kamphaeng Phet", "Bang Sue", "Tao Poon", "Bang Pho", "Bang O", "Bang Yi Khan", "Sirindhorn", "Bang Phlat", "Bang Wa", "Tha Phra")

    print(Station_mrt)
    print(" >> ".join(Station_mrt))
    print(" >> ".join(Station_mrt[1:4]))
    print(" >> ".join(Station_mrt[1:4][::-1]))

def password(lenth):
    s = list("Topgun123")
    p = random.sample(s,lenth)
    return "".join(p)

def replace_demo():
    s = "password"
    s2 = s.replace("a","@")
    print(s2)

    s2 = "password"
    s3 = s2.replace("word","sentence")
    print(s3)


replace_demo()