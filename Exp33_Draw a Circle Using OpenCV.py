import cv2
import numpy as np

# Function to create white image and draw circle
def create_image(width, height):

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate center of image
    center = (width // 2, height // 2)

    # Calculate radius
    radius = min(width, height) // 4

    # Draw a red circle
    cv2.circle(image, center, radius, (0, 0, 255), 3)

    # Display image
    cv2.imshow("White Image with Circle", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Call function
create_image(width, height)
