from confluent_kafka import Consumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient

import config

# Topic
topic = "events"

# Connect to Schema Registry
schema_registry = SchemaRegistryClient(config.schema_registry_conf)

# Load schema
with open("schemas/user_action_schema.json") as f:
    schema_str = f.read()

# Convert dict → Python object
def from_dict(data: dict, ctx: SerializationContext):
    return data  # keep as simple dict

# Create deserializer
deserializer = JSONDeserializer(
    schema_str=schema_str,
    schema_registry_client=schema_registry,
    from_dict=from_dict
)

# Build consumer config dynamically
consumer_conf = config.kafka_conf.copy()
consumer_conf.update({
    "group.id": "G1",
    "auto.offset.reset": "earliest"
})

consumer = Consumer(consumer_conf)
consumer.subscribe([topic])

print("Consumer started. Listening on topic:", topic)

try:
    while True:
        msg = consumer.poll(1)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error:", msg.error())
            continue

        data = deserializer(
            msg.value(),
            SerializationContext(topic, MessageField.VALUE)
        )

        print("Received:", data)

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()
