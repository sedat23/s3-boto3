import boto3

"""
    If you want to set AWS credentials within the file uncomment the following try catch block and comment line below it.
    Please note that this is not a recommended way according to boto3 official documentation.
"""

"""
try:
    s3Client = boto3.resource('s3', region_name='us-east-1',
                              aws_access_key_id='aws_access_key_id', aws_secret_access_key='aws_secret_access_key')
except Exception as e:
    print("Program terminated with the following error: \n" + str(e))
    exit(1)
"""
s3Client = boto3.resource('s3')
s3BucketName = "Your S3 BucketName"

"""
    Head Bucket Call to check if Bucket exists and we've required permissions to perform read/write operations.
"""
try:
    s3Client.head_bucket(Bucket=s3BucketName)
except Exception as e:
    print("Either bucket doesn't exist or you don't have permissions to access it. Find below the error description: \n" + str(e))
    exit(1)

remote_file_path = "File Name along with it's extension. Ex: Archive.zip or /Users/xyz/Desktop/Text.txt.., Full path is not required for files \
                    in Bucket directory. If it is nested under multiple folders key should be given as abc/xyz/pqr.zip, xyz/abc.txt..."
local_output_file_with_path = "Output name of the file, path is not required if you intend to save the file under current directory, \
                                If file needs to be saved in other directory, file name along with path should be given."

try:
    s3Client.Bucket(s3BucketName).download_file(
        remote_file_path, local_output_file_with_path)
except Exception as e:
    print("Either bucket doesn't exist or you don't have permissions to access it. Find below the error description: \n" + str(e))
    exit(1)
