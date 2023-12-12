import cv2
import matploylib.py as plt
img=('',0)
hist_1=cv2.calcHist([img],[0],None,[256],[0,256])
img_2=cv2.equalizeHist(img)
hist_2=cv2.calcHist([img_2],[0],None,[256],[0,256])
plt.subplot(221),plt.imshow(img);
plt.subplot(222),plt.plot(hist_1);
plt.subplot(223),plt.imshow(img_2);
plt.subplot(224),plt.plot(hist_2);