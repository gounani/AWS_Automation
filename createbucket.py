import boto3

s3.create_bucket(Buket='mybucket')
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
