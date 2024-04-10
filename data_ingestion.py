from kafka import KafkaProducer
import json

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Example data for ad impressions in JSON format
ad_impression = {
    "ad_id": "123",
    "user_id": "456",
    "timestamp": "2024-04-10T12:00:00",
    "website": "example.com"
}

# Send ad impressions data to Kafka topic
producer.send('ad_impressions_topic', json.dumps(ad_impression).encode('utf-8'))