from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'demo_testing2',
    bootstrap_servers=['3.145.13.1:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    print(count)
    print(i)
    with s3.open("s3://stock-market-project-hitesh17/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)  