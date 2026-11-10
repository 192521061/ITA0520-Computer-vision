import cv2
import numpy as np

# Function to create image with four coloured boxes
def create_image(width, height):

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate box size (1/10th of image)
    box_width = width // 10
    box_height = height // 10

    # Black box - Top Left Corner
    image[0:box_height, 0:box_width] = (0, 0, 0)

    # Blue box - Top Right Corner
    image[0:box_height, width-box_width:width] = (255, 0, 0)

    # Green box - Bottom Left Corner
    image[height-box_height:height, 0:box_width] = (0, 255, 0)

    # Red box - Bottom Right Corner
    image[height-box_height:height, width-box_width:width] = (0, 0, 255)

    # Display image
    cv2.imshow("Four Coloured Boxes", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Call function
create_image(width, height)
