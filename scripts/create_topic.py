from confluent_kafka.admin import AdminClient, NewTopic
from config import kafka_conf

# Connect to Kafka
admin_client = AdminClient(kafka_conf)

# Define a new topic
topic = NewTopic(
    "events",
    num_partitions=3,
    replication_factor=3
)

# Create topic
fs = admin_client.create_topics([topic])
for topic, f in fs.items():
    try:
        f.result()
        print(f"Topic {topic} created successfully")
    except Exception as e:
        print(f"Failed to create topic {topic}: {e}")