import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(bootstrap_servers=['3.145.13.1:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


df = pd.read_csv("indexProcessed.csv")


while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_testing2', value=dict_stock)
    sleep(1)

producer.flush() #clear data from kafka server , must be used to producer.send 