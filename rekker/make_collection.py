import boto3
import random
import click

def get_b64(image_path):
    image = open(image_path,
                 'rb')  # open binary file in read mode image_read
    image_read = image.read()
    return image_read

def get_r_client():
    return boto3.client('rekognition', region_name='eu-west-1')

def create_collection(client,collection_id):
    path = "data/collection/"
    image_path = path + "image.jpg"
    print(path + "and my new collection is: " + collection_id)

    client.create_collection(CollectionId=collection_id)

    response = client.index_faces(
        CollectionId=collection_id,
        Image={'Bytes': get_b64(image_path)},
        ExternalImageId='my_string',
        DetectionAttributes=[
            'DEFAULT'
        ],
        MaxFaces=1,
        QualityFilter='NONE'
    )
    print(response)

    return collection_id

def delete_collection(client,collection):
    print(client.delete_collection(CollectionId=collection))

@click.command()
@click.option('--collection-id', help='Your picture file')
def main(collection_id):
    c = get_r_client()
    delete_collection(c,collection_id)
    print("creating a collection...")
    new_coll = create_collection(c,collection_id)
    delete_collection(c,new_coll)

if __name__ == "__main__":
    main()