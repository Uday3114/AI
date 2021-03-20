import numpy
import cv2

img = cv2.imread("birthday.PNG")
cv2.imwrite("birthdayCopy.PNG",img)
cv2.imshow("birthday1",img)

cv2.waitKey(0)
cv2.destroyAllWindows()