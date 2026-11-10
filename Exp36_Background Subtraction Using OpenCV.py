import cv2
import numpy as np

# Function for background subtraction
def remove_background(image_path):

    # Read input image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define background colour range (green)
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Create mask for green background
    mask = cv2.inRange(hsv, lower, upper)

    # Remove background
    result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

    # Display original image
    cv2.imshow("Original Image", image)

    # Display background mask
    cv2.imshow("Background Mask", mask)

    # Display final image
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image path from user
image_path = input("Enter image path: ").strip().strip('"')

# Call function
remove_background(image_path)
