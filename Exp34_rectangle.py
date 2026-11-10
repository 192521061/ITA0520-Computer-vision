import cv2
import numpy as np

# Function to create white image and draw rectangle
def create_image(width, height):

    # Create white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw red rectangle
    cv2.rectangle(image, (50, 50),
                  (width-50, height-50),
                  (0, 0, 255), 3)

    # Display image
    cv2.imshow("White Image with Rectangle", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Call function
create_image(width, height)
