# import boto3
# import sys

# # Initialize a Boto3 S3 client
# s3 = boto3.client('s3')

# def list_bucket_contents(boto890):
#     try:
#         # Check if the bucket exists
#         s3.head_bucket(Bucket=bucket_name)

#         # List objects (files) in the specified S3 bucket
#         response = s3.list_objects(Bucket=bucket_name)

#         # Check if objects exist in the bucket
#         if 'Contents' in response:
#             print(f"Objects in '{bucket_name}':")
#             for obj in response['Contents']:
#                 print(obj['Key'])
#         else:
#             print(f"No objects found in '{bucket_name}'.")
#     except s3.exceptions.ClientError as e:
#         if e.response['Error']['Code'] == '404':
#             print(f"Bucket '{bucket_name}' does not exist.")
#         else:
#             print(f"An error occurred: {e}")

# if len(sys.argv) != 2:
#     print("Usage: python script_name.py <bucket_name>")
# else:
#     bucket_name = sys.argv[1]
#     list_bucket_contents(bucket_name)
import boto3

def list_bucket_contents(bucket_name):
    # Initialize a Boto3 S3 client
    s3 = boto3.client('s3')

    try:
        # Check if the bucket exists
        s3.head_bucket(Bucket=bucket_name)

        # List objects (files) in the specified S3 bucket
        response = s3.list_objects(Bucket=bucket_name)

        # Check if objects exist in the bucket
        if 'Contents' in response:
            print(f"Objects in '{bucket_name}':")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No objects found in '{bucket_name}'.")
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Bucket '{bucket_name}' does not exist.")
        else:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user to enter the S3 bucket name
    bucket_name = input('Enter the name of the S3 bucket: ')
    
    # Call the function to list bucket contents
    list_bucket_contents(bucket_name)
