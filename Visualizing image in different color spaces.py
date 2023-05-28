# # Python program to read image
# # as YCrCb color space
#
# # Import cv2 module
# import cv2
#
# # Reads the image
# img = cv2.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources//salu.jpg')
#
# # Convert to YCrCb color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#
# # Shows the image
# cv2.imshow('image', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#


#################### 2nd code ##########################################













# Python program to read image
# as HSV color space

# Importing cv2 module
import cv2

# Reads the image
img = cv2.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources//salu.jpg')

# Converts to HSV color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Shows the image
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

