import cv2
import numpy as np

img = cv2.imread('assets/tree.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:, :, 0] = np.where(
    (hsv[:, :, 0] >= 35) & (hsv[:, :, 0] <= 75), (hsv[:, :, 0] + 145) % 180 , hsv[:, :, 0]
)
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('assets/output_main.jpg', bgr)
