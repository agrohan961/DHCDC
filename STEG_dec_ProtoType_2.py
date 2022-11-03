import cv2

def bintohex(text):
    return hex(int(text,2))[2:]

def desteg(img):
    data = ''

    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(len(img[0][0])):
                data += ("{:0b}".format(int(img[i][j][k])))[-1]
                if((len(data) % 8 == 0) and (data[-1:-9:-1] == "00000000")):
                    return data[:len(data)-8]
print(bintohex(desteg(cv2.imread("test1.png"))))
                