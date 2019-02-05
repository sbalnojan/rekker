# get video from cam
import  cv2
import random
import rekker.get_face_info as rek

def identify_face(image):
    rek.main_fn(image)

def capture_vid():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    output_file_name = "data/output_video_"+ str(random.randrange(1, 10000)) + ".avi"
    out = cv2.VideoWriter(output_file_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    count = 0

    while (True):
        ret, frame = cap.read()

        if ret == True:

            # Write the frame into the file 'output.avi'
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite("data/frame_last.jpg", frame)
                identify_face("frame_last.jpg")

            if cv2.waitKey(1) & 0xFF == ord('w'):
                cv2.imwrite("data/frame_last.jpg", frame)
                break
        # Break the loop
        else:
            break

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()

def clean_folder()

def main():

    clean_folder("data")
    capture_vid()


if __name__ == "__main__":
    main()