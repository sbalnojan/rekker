# get video from cam
import  cv2
import random
# Create a VideoCapture object and read from input file
# If the input is taken from the camera, pass 0 instead of the video file name.


def capture_vid():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    output_file_name = "data/raw/video-proto/outpy"+ str(random.randrange(1, 10000)) + ".avi"
    out = cv2.VideoWriter(output_file_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    count = 0

    while (True):
        ret, frame = cap.read()
        cv2.imwrite("data/raw/video-proto/frame%d.jpg" % count, frame)
        count += 1

        if ret == True:

            # Write the frame into the file 'output.avi'
            out.write(frame)

            cv2.imshow('window-name', frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

            # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()

def main():

    cap = capture_vid()

if __name__ == "__main__":
    main()