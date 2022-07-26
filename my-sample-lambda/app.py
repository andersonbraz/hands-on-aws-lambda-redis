import boto3
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('braz-bucket-storage')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object)