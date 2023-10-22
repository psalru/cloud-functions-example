import os
import time
import boto3
from datetime import datetime
from gen import gen_content, gen_report


def get_boto_session():
    boto_session = boto3.session.Session(
        aws_access_key_id=os.environ['ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']
    )

    return boto_session


def get_storage_client(region='ru-central1'):
    storage_client = get_boto_session().client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        region_name=region
    )

    return storage_client


def handler(event, context):
    args = event['queryStringParameters']

    if 'id' not in args.keys() or not args['id'].isnumeric():
        raise Exception('Params university ID is required')

    args['folder'], args['width'] = '/tmp', 13
    object_name = f"reporting/vacancies/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_id_{args['id']}.docx"

    start = time.time()
    gen_content(args)
    file_path = gen_report(args)
    client = get_storage_client()
    client.upload_file(file_path, 'psal.public', object_name)

    return {
        'statusCode': 302,
        'headers': {
            'Location': client.generate_presigned_url('get_object', Params={
                'Bucket': 'psal.public',
                'Key': object_name
            }, ExpiresIn=3600)
        },
        'body': {
            "generated_by": f"{round(time.time() - start, 2)} second",
            "ulr": client.generate_presigned_url('get_object', Params={
                'Bucket': 'psal.public',
                'Key': object_name
            }, ExpiresIn=3600)
        }
    }
