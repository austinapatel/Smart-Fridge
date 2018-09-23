import boto
import boto.s3
import sys
from boto.s3.key import Key


AWS_ACCESS_KEY_ID = open('AWS_ACCESS_KEY_ID.txt').read()
AWS_SECRET_ACCESS_KEY = open('AWS_SECRET_ACCESS_KEY.txt').read()

bucket_name = 'smart-fridge-basehacks'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.get_bucket(bucket_name)

testfile = "image.jpg"
print('Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

# add new file
k = Key(bucket)
k.key = testfile
k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)