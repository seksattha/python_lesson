def thai_rai(sqwa):
    rai = sqwa // 400
    ngan = (sqwa-(rai*400)) // 10
    wa = sqwa % 100
    return rai,ngan,wa

if __name__ == '__main__':
    a = 956
    print(thai_rai(a))
    #จะได้ค่าออกมาเป็น Tuple

    # หรือว่าจะแสดงผลแบบนี้ก็ได้
    r,n,w = thai_rai(a)
    print(r,n,w,sep="-")

