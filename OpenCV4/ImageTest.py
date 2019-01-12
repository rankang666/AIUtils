import numpy as np
import cv2 as cv

# 加载一个图片，第二个参数加载图片类型:
#    cv.IMREAD_COLOR : 1  Loads a color image. Any transparency of image will be neglected. It is the default flag.
#    cv.IMREAD_GRAYSCALE : 0  Loads image in grayscale mode
#    cv.IMREAD_UNCHANGED : -1 Loads image as such including alpha channel
#    Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

img = cv.imread("girl.jpg",0)
# 展示，参数: 窗口名字，图片文件
# cv.imshow("image", img)

# 当已经创建了一个窗口，之后加载一个图片，第二个参数觉得你是否重新设置window的大小，默认为cv.WINDOW_AUTOSIZE.
# cv.namedWindow("image", cv.WINDOW_NORMAL)

# 保存一个图片
# cv.imwrite("mess_gray.png",img)

# 通过输入按键，执行
#If you are using a 64-bit machine, you will have to modify k = cv.waitKey(0) line
#   as follows : k = cv.waitKey(0) & 0xFF
'''
k = cv.waitKey(0) & 0xFF
if k == 27 :    # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('mess.png',img)
    cv.destroyAllWindows()
'''

# 停留时间 默认: 毫秒，0为不关闭
# cv.waitKey(2000)
# 关闭我们创建的窗口
# cv.destroyWindow()
# 关闭我们创建的所有窗口
# cv.destroyAllWindows()


# Using Matplotlib
# Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.
# So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.
from matplotlib import pyplot as plt
# img = cv.imread("girl.jpg",0)
img = cv.imread("girl.jpg",1)
# 将BGR转为RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]),plt.yticks([])   # to hide tick values on X and Y axis
plt.show()