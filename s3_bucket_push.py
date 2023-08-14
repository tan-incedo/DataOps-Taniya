import boto3

# Specify your AWS credentials
aws_access_key = ''
aws_secret_key = ''

# Specify the S3 bucket and folder path
bucket_name = 'bkt-'
folder_path = 'input'

# List of local file paths to upload
local_file_paths = ['path/to/your/local/file1.txt', 'path/to/your/local/file2.txt']

# Create a Boto3 S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Upload each file to the S3 bucket folder
for local_file_path in local_file_paths:
    file_name = local_file_path.split('/')[-1]  # Extract the file name
    s3_key = folder_path + file_name  # S3 object key (path within the bucket)
    
    s3_client.upload_file(local_file_path, bucket_name, s3_key)