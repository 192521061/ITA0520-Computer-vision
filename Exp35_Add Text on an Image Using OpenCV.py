import cv2

# Function to add text on an image
def add_text(image_path, text):

    # Read the input image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Add text on the image
    cv2.putText(image, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    # Display the image
    cv2.imshow("Text on Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image path from user
image_path = input("Enter image path: ")

# Get text from user
text = input("Enter text to display: ")

# Call function
add_text(image_path, text)
