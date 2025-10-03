from confluent_kafka import Consumer
import json, os, asyncio

conf = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP", "kafka:29092"),
    "group.id": "processor-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)

async def consume_events(topic):
    consumer.subscribe([topic])
    loop = asyncio.get_event_loop()
    while True:
        msg = await loop.run_in_executor(None, consumer.poll, 1.0)
        if msg is None or msg.error():
            continue
        yield json.loads(msg.value().decode("utf-8"))
