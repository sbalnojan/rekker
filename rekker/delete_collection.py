import boto3
import click


def get_r_client():
    return boto3.client('rekognition', region_name='eu-west-1')

def delete_collection(client,collection):
    print(client.delete_collection(CollectionId=collection))

@click.command()
@click.option('--collection-id', help='Your picture file')
def main(collection_id):
    c = get_r_client()
    delete_collection(c,collection_id)

if __name__ == "__main__":
    main()