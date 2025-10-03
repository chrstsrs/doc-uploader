from confluent_kafka import Producer
import json, os

conf = {"bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP", "kafka:29092")}
producer = Producer(conf)

def publish_event(topic, event):
    producer.produce(topic, json.dumps(event).encode("utf-8"))
    producer.flush()
