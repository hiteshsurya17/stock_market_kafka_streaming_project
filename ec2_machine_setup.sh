scp -i stock-market-ec2.pem stock-market-ec2.pem ubuntu@ec2-18-222-86-3.us-east-2.compute.amazonaws.com:~/
ssh -i ~/Downloads/stock-market-ec2.pem ubuntu@ec2-18-222-86-3.us-east-2.compute.amazonaws.com
wget https://downloads.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xvf kafka_2.13-3.7.0.tgz
sudo apt update
sudo apt install openjdk-8-jdk
java -version
cd kafka_2.13-3.7.0/
sudo nano config/server.properties
advertised.listeners = PLAINTEXT://18.222.86.3:9092


bin/zookeeper-server-start.sh config/zookeeper.properties

export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties

bin/kafka-topics.sh --create --bootstrap-server 18.222.86.3:9092 --topic demo_testing2 --replication-factor 1 --partitions 1

bin/kafka-console-producer.sh --broker-list 18.222.86.3:9092 --topic demo_testing2

bin/kafka-console-consumer.sh --bootstrap-server 18.222.86.3:9092 --topic demo_testing2
