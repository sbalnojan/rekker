# rekker

```bash
- main.py             # runs the "simple setup"
--rekker
--- get_face_info.py  # aws rek. functions to get info on face image
--examples
--- get_video.py      # script to capture video to file w. frame pics.
```

### The Simple Setup

Have a laptop somewhere with a camera; Have it run ... .

- someone approaches the camera. The video feedback is running.
- he hits the key "q" to capture the displayed frame.
- the voice appears and says "..."
- hit "w" to stop the recording.

### The Identifier Setup

- To set this up, put your collection into data/collection
- Then run `bash make coll`

- Same thing, except the voice returns "Hi I don't know you" or
  "Hi X".
- Someone has previously executed script "..." to create the collection.

### The Automatic Setup

- This all works automatically, while people are walking by...
- Frames are captured every 2 secs.

## Requirements

- The voiceout requires a computer with mpg321 installed.
- Python 3.X

## The scripts

Get some images from the video cam.

```bash
python3 get_video.py
```

Will save some images into /data/....

Get some face info:

```
python3 get_face_info.py --
```

# To Do

- The Identifier Setup
- The Automatic Setup
