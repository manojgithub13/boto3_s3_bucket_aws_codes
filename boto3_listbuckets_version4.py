import boto3

def get_s3_bucket_regions():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    bucket_regions = {}

    for bucket in buckets:
        bucket_name = bucket['Name']
        region = s3.get_bucket_location(Bucket=bucket_name).get('LocationConstraint', 'us-east-1')
        bucket_regions[bucket_name] = region

    return bucket_regions

def write_to_file(data):
    with open('s3_bucket_regions.txt', 'w') as file:
        for bucket, region in data.items():
            file.write(f"Bucket Name: {bucket}\tRegion: {region}\n")

if __name__ == "__main__":
    bucket_regions = get_s3_bucket_regions()
    write_to_file(bucket_regions)
    print("Bucket regions saved to s3_bucket_regions.txt")
