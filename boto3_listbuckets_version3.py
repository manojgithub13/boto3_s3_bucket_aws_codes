import boto3

def list_buckets_containing_file(filename):
    # Initialize a Boto3 S3 client
    s3 = boto3.client('s3')

    try:
        # Get the list of all S3 buckets
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        # Check each bucket for the presence of the file
        buckets_with_file = []
        for bucket_name in buckets:
            try:
                s3.head_object(Bucket=bucket_name, Key=filename)
                buckets_with_file.append(bucket_name)
            except s3.exceptions.ClientError as e:
                if e.response['Error']['Code'] != '404':
                    print(f"An error occurred while checking {bucket_name}: {e}")

        # Print the buckets containing the file
        if buckets_with_file:
            print(f"The file '{filename}' is present in the following buckets:")
            for bucket_name in buckets_with_file:
                print(bucket_name)
        else:
            print(f"The file '{filename}' is not present in any of the buckets.")
    except s3.exceptions.ClientError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user to enter the filename
    filename = input('Enter the filename to search: ')
    
    # Call the function to list buckets containing the file
    list_buckets_containing_file(filename)
