import cv2
import numpy as np

source = cv2.imread('/home/nhs/EL4S/myapp/public/images/image.jpg')
for i in range(17):
    hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = np.where(
        (hsv[:, :, 0] >= 35) & (hsv[:, :, 0] <= 75), (i * 10), hsv[:, :, 0]
    )
    output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite('/home/nhs/EL4S/myapp/public/images/output_'+str(i)+'.jpg', output)
