import cv2

def hextobin(num):
    return "".join(['{:04b}'.format(int(x,16)) for x in num])
def steg(img, text):
    length = len(text)
    temp = 0
    binlen = '{:030b}'.format(length)

    for i in range(-1,-11,-1):
        for j in range(3):
            img[0][i][j] = int((('{:0b}'.format(int(img[0][i][j])))[:-1]+binlen[0]),2)
            binlen = binlen[1:]

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = int((('{:0b}'.format(int(img[i][j][k])))[:-1]+text[0]),2)
                text = text[1:]
                temp += 1
                if (temp == length):
                    return img

text = "ca4d3b539be107eb86e8f83afba1ca8ddb7ee4bad1fdbfdbbd46059f4023ed8e9bfa61d757ba5540c557ccdf8f80a40b54cf1b1647cd2757dd078e11d2933ad8d09cfa7c648f9aebb08b9526447e4ebae40cce5845418fcfc2d774a73eaedf7e9311b965b5c49e89b7209cf8258608a6837dc6d2c6d4649b95cdbf86b379a78021fb7b833f7bf8ad85f887f33f2df5190dbf6661168a51f48961ac0c3a45a301e844aee43125e2947b2d3a8d751b4c3e97f824fbfd6e6c1d70d374829b104bf69064ab0af6d8faea0d791324db786e82dc3cb037400abbd9fa39dca1d240489b455cbf4653e42d3c67de31bc9da1c5b881350d8cfa50a1334606f204e1ac00c8ccf2867a097c72a4735fc9a9a7d32f27c58adee3110f616044c945bb736aa0a4149c0e63f1bccdeab664862278ea9336ffa0255c3eb4da499f6a18800791f294f7f014f03e33f44faa3133644664e238781d8de9bb28e25a5b57cc36323e0a608b7052ba0e81ddd035bb299fbadca2ef7b2d3a8d751b4c3ef5ccd66983556abdc6932953625e885d04af11b5992ea765c36f5dc92e4cd47833cb5613094877e6319f8d48111656df12ef85b22f48c79c5bbcf11c79731a6c"
text = hextobin(text)
print(text)
image = steg(cv2.imread('TEST.png'), text)

cv2.imwrite("TEST1.png",image)