import cv2

def reverse_slow_motion(video_path):

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video not found!")
        return

    frames = []

    # Read all video frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Play frames in reverse order
    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion Video", frame)

        # Delay of 100 milliseconds for slow motion
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Get video path
video_path = input("Enter video path: ").strip().strip('"')

reverse_slow_motion(video_path)
