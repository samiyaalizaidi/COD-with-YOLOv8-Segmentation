import boto3
import botocore

BUCKET_NAME = "cod-ash"

# enter authentication credentials
s3 = boto3.resource('s3', aws_access_key_id = "",
                          aws_secret_access_key= "")

KEY = "YOLOv8-Combined-Split.zip" # replace with your object key

try:
  s3.Bucket(BUCKET_NAME).download_file(KEY, "/Downloads/YOLOv8-Combined-Split.zip")

except botocore.exceptions.ClientError as e:
  if e.response['Error']['Code'] == "404":
    print("The object does not exist.")
  else:
    raise

