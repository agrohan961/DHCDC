import cv2

def bintohex(text):
    return hex(int(text,2))[2:]
    
def desteg(img):
    length = ''
    data = ''
    temp = 0

    for i in range(-1,-11,-1):
        for j in range(3):
            length += ('{:0b}'.format(int(img[0][i][j])))[-1]
    
    length = int(length,2)

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                data += ('{:0b}'.format(int(img[i][j][k])))[-1]
                temp += 1
                if (temp == length):
                    return data

print(bintohex(desteg(cv2.imread("test1.png"))))
