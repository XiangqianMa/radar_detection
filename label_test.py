import cv2

image = cv2.imread("111.jpg")
print(image)
cv2.namedWindow("imshow")
cv2.imshow("image", image)
cv2.waitKey(0)
