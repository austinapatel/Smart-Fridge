# import boto
import sys


AWS_ACCESS_KEY_ID = open('AWS_ACCESS_KEY_ID.txt').read()
AWS_SECRET_ACCESS_KEY = open('AWS_SECRET_ACCESS_KEY.txt').read()

bucket_name = 'smart-fridge-basehacks'
# conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

testfile = "image.jpg"
print('Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

# bucket = conn.get_bucket(bucket_name)

# # add new file
# k = Key(bucket)
# k.key = testfile
# k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)


import boto3
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

s3 = session.resource('s3')
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read().decode("utf-8")
    print(body)


#
# key = obj.key
# body = obj.get()['Body'].read()
# print(body)