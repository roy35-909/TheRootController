import boto3

def list_s3_buckets(region_name):
    s3 = s.client('s3', region_name=region_name)
    try:
        response = s3.list_buckets()
        print(f"Buckets in region {region_name}:")
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing S3 buckets in region {region_name}: {e}")

def delete_all_s3_buckets(region_name):
    s3 = s.client('s3', region_name=region_name)
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            try:
                # Empty the bucket
                print(f"Emptying bucket: {bucket_name}")
                bucket_resource = s.resource('s3').Bucket(bucket_name)
                bucket_resource.objects.all().delete()
                bucket_resource.object_versions.all().delete()

                # Delete the bucket
                print(f"Deleting bucket: {bucket_name}")
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Bucket {bucket_name} deleted successfully.")
            except Exception as e:
                print(f"Error deleting bucket {bucket_name}: {e}")
    except Exception as e:
        print(f"Error fetching S3 buckets in region {region_name}: {e}")

def get_all_regions():
    ec2 = s.client('ec2')
    try:
        response = ec2.describe_regions()
        regions = [region['RegionName'] for region in response['Regions']]
        return regions
    except Exception as e:
        print(f"Error fetching regions: {e}")
        return []

if __name__ == "__main__":
    profile_names = ['group-1', 'group-2', 'group-3', 'ostad-1', 'ostad-2', 'ostad-3', 'ostad-4']
    for j in profile_names:
        print(f"We Are In : {j}")
        s = boto3.Session(profile_name=j)
        all_regions = get_all_regions()
        for i in all_regions:
            print(f'Doing Operation in Profile: {j} in Region: {i}')
            list_s3_buckets(i)
            delete_all_s3_buckets(i)
            list_s3_buckets(i)