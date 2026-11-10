import cv2

def count_faces(image_path):

    # Load the input image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count the detected faces
    count = len(faces)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image, (x, y), (x+w, y+h),
            (0, 255, 0), 2
        )

    # Display face count
    print("Number of faces detected:", count)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get image path
image_path = input("Enter image path: ").strip().strip('"')

count_faces(image_path)
