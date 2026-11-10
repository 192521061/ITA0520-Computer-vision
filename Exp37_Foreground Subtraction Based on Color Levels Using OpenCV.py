import cv2
import numpy as np

def subtract_foreground(image_path):

    # Read the input image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color levels (green color)
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Create a mask based on color levels
    mask = cv2.inRange(hsv, lower, upper)

    # Extract foreground by removing green areas
    foreground = cv2.bitwise_and(
        image, image, mask=cv2.bitwise_not(mask)
    )

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Mask", mask)
    cv2.imshow("Foreground", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image path from user
image_path = input("Enter image path: ").strip().strip('"')

subtract_foreground(image_path)
