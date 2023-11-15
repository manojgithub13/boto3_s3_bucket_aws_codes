import boto3

s3 = boto3.client('s3')

bucket_name = input('Enter the name of the S3 bucket: ')

try:
    response = s3.list_objects(Bucket=bucket_name)

    if 'Contents' in response:
        print(f"Objects in '{bucket_name}':")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f"No objects found in '{bucket_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
