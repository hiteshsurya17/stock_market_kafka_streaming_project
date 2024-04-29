from s3fs import S3FileSystem
import json

s3 = S3FileSystem()

count=1 
value = 'test'
with s3.open("s3://stock-market-project-hitesh17/stock_market_{}.json".format(count), 'w') as file:
        json.dump(value, file)