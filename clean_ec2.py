import boto3

def list_ec2_instances(region_name):
    ec2 = s.client('ec2', region_name=region_name)
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Region: {region_name}")
                print(f"Instance ID: {instance['InstanceId']}")
                print(f"State: {instance['State']['Name']}")
                print(f"Instance Type: {instance['InstanceType']}")
                print(f"Public DNS: {instance.get('PublicDnsName', 'N/A')}")
                print(f"Private IP: {instance.get('PrivateIpAddress', 'N/A')}")
                print("-" * 60)
    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")

def delete_all_ec2_instances(region_name):
    ec2 = s.client('ec2', region_name=region_name)
    try:
        response = ec2.describe_instances()
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])
        
        if instance_ids:
            print(f"Terminating instances: {instance_ids}")
            ec2.terminate_instances(InstanceIds=instance_ids)
            print("Termination initiated.")
        else:
            print("No instances found to terminate.")
    except Exception as e:
        print(f"Error deleting EC2 instances: {e}")

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
    profile_names = ['group-1', 'group-2', 'group-3','ostad-1','ostad-2','ostad-3','ostad-4']
    for j in profile_names:
        print(f"We Are In : {j}")
        s = boto3.Session(profile_name=j)
        all_regions = get_all_regions()
        for i in all_regions:
            print(f'Doing Operation in Profile: {j} in Region: {i}')
            list_ec2_instances(i)
            delete_all_ec2_instances(i)
            list_ec2_instances(i)



