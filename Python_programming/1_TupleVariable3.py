"!!! Important tuple is immutable variable"
"Do not change after create tuple variable"

def distance(pointA, pointB):
    return ((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)**.5

if __name__ == '__main__':
    x = 3,15
    y = 7,20

#using tuple variable making the code cleaner and more readable.
d = distance(x,y)
print("Distance = {}".format(d))

