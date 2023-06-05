# import cv2 library
import cv2
# import required module
import os


def getFiles(curDir):
    all = []
    # iterate over files in dir_work
    for filename in os.listdir(curDir):
        f = os.path.join(curDir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            all.append(cv2.imread(f))

    return all

def setBorder(img):
    pad_top = pad_bot = pad_left = pad_right = 2
    padColor = [255, 255, 255]
    img = cv2.copyMakeBorder(img, pad_top, pad_bot, pad_left, pad_right, cv2.BORDER_CONSTANT, None,padColor)
    return img

def getFilesWithCalc(curDir, calc):
    all = getFiles(curDir)
    calc = cv2.imread(calc)
    i = 0
    while (i < len(all)):
        all[i] = cv2.addWeighted(all[i], 1, calc, (175/255), 1)
        i += 1
    return all

# assign base directory
dir_work = '../img-src/biomes'
dir_static = '../static/biomes'
dir_out = '../img-output/'

all = []
all += getFilesWithCalc(dir_work + '/blue', dir_static + '/calc-blue.png')
all += getFilesWithCalc(dir_work + '/green', dir_static + '/calc-green.png')
all += getFilesWithCalc(dir_work + '/yellow', dir_static + '/calc-yellow.png')
all += getFilesWithCalc(dir_work + '/red', dir_static + '/calc-red.png')
all += getFilesWithCalc(dir_work + '/black', dir_static + '/calc-black.png')

while(len(all) % 4 != 0):
    all.append(cv2.imread(dir_static+'/default.png'))

# Apply White Border
i=0
while (i < len(all)):
    all[i] = setBorder(all[i])
    i += 1

combined = []
i=0
while (i < len(all)):
    im_vA = cv2.hconcat([all[i], all[i+1]])
    im_vB = cv2.hconcat([all[i+2], all[i+3]])
    combined.append(cv2.vconcat([im_vA, im_vB]))
    i = i+4

i=0
for img in combined :
    # A4 standard landscape : 3510 * 2490
    # img size landscape : 3072 * 2048
    # border : 2px top/down * 2 pic & 2px left/right * 2 pic => 8 & 8
    pad_top = pad_bot =  int((2490 - 2048 - 8) / 2)
    pad_left = pad_right = int((3510 - 3072 - 8) / 2)
    padColor = [255, 255, 255]
    img = cv2.copyMakeBorder(img, pad_top, pad_bot, pad_left, pad_right, cv2.BORDER_CONSTANT, None,padColor)

    cv2.imwrite(dir_out + 'a4_bi_'+str(i)+'.jpg', img)
    i += 1
