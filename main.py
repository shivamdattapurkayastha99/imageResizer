import cv2
src=cv2.imread("logoimg.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)

scale_percent = 50

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)


dsize = (width, height)


output = cv2.resize(src, dsize)

cv2.imwrite('newImage.png',output) 
cv2.waitKey(0)



