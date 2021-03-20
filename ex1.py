import numpy
import cv2

img = cv2.imead("uday.jpg")
cv2.imwrite("udayCopy.jpg",img)
cv2.imshow("uday",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
