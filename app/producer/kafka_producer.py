import json
from confluent_kafka import Producer
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from config import kafka_conf, schema_registry_conf

# Topic name
TOPIC = "events"

# Load schema
with open("schemas/user_action_schema.json") as f:
    schema_str = f.read()

# Connect to Schema Registry
schema_registry = SchemaRegistryClient(schema_registry_conf)
serializer = JSONSerializer(schema_str, schema_registry)


# Kafka producer
producer = Producer(kafka_conf)

def produce_event(event_data: dict):
    """
    Sends a single event to Kafka.
    """
    producer.produce(
        topic=TOPIC,
        value=serializer(event_data, SerializationContext(TOPIC, MessageField.VALUE))
    )
    producer.flush()