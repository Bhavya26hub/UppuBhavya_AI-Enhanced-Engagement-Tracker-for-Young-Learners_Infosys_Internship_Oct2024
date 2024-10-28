import cv2

# Load the colored image
realimage = cv2.imread("C:\\Users\\uppub\\OneDrive\\Pictures\\Camera Roll\\download.jpg")
image = cv2.imread("C:\\Users\\uppub\\OneDrive\\Pictures\\Camera Roll\\download.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('grayscale_image.jpg', gray_image)

# Display the grayscale image
cv2.imshow("Original Image",realimage)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
