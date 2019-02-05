import boto3
import base64
import json
from gtts import gTTS
from io import BytesIO
import os
import numpy as np
import click

def get_r_client():
    return boto3.client('rekognition', region_name='eu-west-1')

def get_b64(image_path):
    image = open(image_path,
                 'rb')  # open binary file in read mode image_read
    image_read = image.read()
    return image_read

def get_face_info(image_path,client):
    response = client.detect_faces(Attributes=['ALL'], Image={'Bytes': get_b64(image_path)})
    print('Detected face info in in ' + image_path)
    print('Done...')

    return response

def v_o_emotions(sentence):
    mp3_file = "say_this.mp3"
    tts = gTTS(text=sentence, lang='en')
    tts.save(mp3_file)

    os.system("mpg321 " + mp3_file)

def desc_sort_list(list, key):
    """desc sort list of dicts for a given key."""
    return sorted(list, key=lambda kev: kev[key], reverse=True)

def make_emo_sentence(list):

    list = desc_sort_list(list,"Confidence")[:3]
    sentence = ''
    for item in list:
        sentence += f"I feel {np.round(item['Confidence'],1)} percent confident, that you are {item['Type']}. "
    return sentence

def main_fn(file):
    image_path = "data/" + file
    print(f"Retrieving info for {image_path}")

    client = get_r_client()
    resp = get_face_info(image_path,client)
    if (len(resp["FaceDetails"]) >= 2):
        v_o_emotions("Hey, there's two of you!")
    else:
        face = resp["FaceDetails"][0]
        #print(face)
        for emotion in face['Emotions']:
            print(emotion)

        v_o_emotions(make_emo_sentence(face["Emotions"]))

@click.command()
@click.option('--file', help='Your picture file', prompt="your pic")
def main(file):
    main_fn(file)

if __name__ == "__main__":
    file = "frame9.jpg"
    main()
