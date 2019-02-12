import boto3

"""
    If you want to set AWS credentials within the file uncomment the following try catch block and comment line below it.
    Please note that this is not a recommended way according to boto3 official documentation.
"""

"""
try:
    s3 = boto3.client('s3', region_name=region, aws_access_key_id='aws_access_key_id', aws_secret_access_key='aws_secret_access_key')
except Exception as e:
    print("Program terminated with the following error: \n" + str(e))
    exit(1)
"""
s3Client = boto3.client('s3')
s3BucketName = "S3 Bucket Name."

"""
    Head Bucket Call to check if Bucket exists and we've required permissions to perform read/write operations.
"""
try:
    s3Client.head_bucket(Bucket=s3BucketName)
except Exception as e:
    print("Either bucket doesn't exist or you don't have permissions to access it. Find below the error description: \n" + str(e))
    exit(1)

file_with_path = "File Name along with it's extension. Ex: Archive.zip or /Users/xyz/Desktop/Text.txt.., Full path is not required for files \
                    in current directory."
finalOutputFileName = "Name of the file on S3 Bucket. If you want to place this file under existing folders for create new folders and upload, \
                       provide the path here. Ex: abc/cd/finalFileName.zip, subFolderInbucket/FinalTextFile.txt... Note that extension is \
                        part of outputfile name, boto3/s3 wouldn't infer the file extension, that has to be provided."

s3Client.upload_file(file_with_path,s3BucketName,finalOutputFileName)
