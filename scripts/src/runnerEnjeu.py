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

# assign base directory
dir_work = '../img-src/enjeu'
dir_static = '../static/enjeu'
dir_out = '../img-output/'

all = []
all += getFiles(dir_work)
while(len(all) % 40 != 0):
    all.append(cv2.imread(dir_static+'/default.png'))

#Resize 400*400
# & Apply White Border
i = 0
while (i < len(all)):
    all[i] = cv2.resize(all[i], (400,400), cv2.INTER_AREA)
    all[i] = setBorder(all[i])
    i += 1

combinedEnjeu = []
i=0
while (i < len(all)):
    j = 0
    im_vA = cv2.hconcat([all[i+j], all[i+1+j], all[i+2+j], all[i+3+j], all[i+4+j], all[i+5+j], all[i+6+j], all[i+7+j]])
    j = 1*8
    im_vB = cv2.hconcat([all[i+j], all[i+1+j], all[i+2+j], all[i+3+j], all[i+4+j], all[i+5+j], all[i+6+j], all[i+7+j]])
    j = 2*8
    im_vC = cv2.hconcat([all[i+j], all[i+1+j], all[i+2+j], all[i+3+j], all[i+4+j], all[i+5+j], all[i+6+j], all[i+7+j]])
    j = 3*8
    im_vD = cv2.hconcat([all[i+j], all[i+1+j], all[i+2+j], all[i+3+j], all[i+4+j], all[i+5+j], all[i+6+j], all[i+7+j]])
    j = 4*8
    im_vE = cv2.hconcat([all[i+j], all[i+1+j], all[i+2+j], all[i+3+j], all[i+4+j], all[i+5+j], all[i+6+j], all[i+7+j]])
 
    combinedEnjeu.append(cv2.vconcat([im_vA, im_vB, im_vC, im_vD, im_vE]))
    i = i+40

i=0
for img in combinedEnjeu :
    # A4 standard landscape : 3510 * 2490
    # img size landscape : 3200 * 2000  (8 & 5 * 400/400)
    # border : 2px top/down * 5 pic & 2px left/right * 8 pic => 20 & 32
    pad_top = pad_bot = int((2490 - 2000 - 20) / 2)
    pad_left = pad_right = int((3510 - 3200 - 32) / 2)
    padColor = [255, 255, 255]
    img = cv2.copyMakeBorder(img, pad_top, pad_bot, pad_left, pad_right, cv2.BORDER_CONSTANT, None,padColor)

    cv2.imwrite(dir_out + 'a4_enj_'+str(i)+'.jpg', img)
    i += 1
