import boto3

def list_eks_clusters(region_name):
    eks = s.client('eks', region_name=region_name)
    try:
        response = eks.list_clusters()
        print(f"EKS Clusters in region {region_name}:")
        for cluster in response['clusters']:
            print(f"  - {cluster}")
    except Exception as e:
        print(f"Error listing EKS clusters in region {region_name}: {e}")

def delete_all_eks_clusters(region_name):
    eks = s.client('eks', region_name=region_name)
    try:
        response = eks.list_clusters()
        for cluster_name in response['clusters']:
            try:
                print(f"Deleting EKS cluster: {cluster_name}")
                eks.delete_cluster(name=cluster_name)
                print(f"EKS cluster {cluster_name} deleted successfully.")
            except Exception as e:
                print(f"Error deleting EKS cluster {cluster_name}: {e}")
    except Exception as e:
        print(f"Error fetching EKS clusters in region {region_name}: {e}")

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
            list_eks_clusters(i)
            delete_all_eks_clusters(i)
            list_eks_clusters(i)