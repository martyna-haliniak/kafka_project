### Project Architecture Overview
This project simulates a real-time event streaming pipeline using **FastAPI**, **Kafka**, **Schema Registry**, and a **mock client** that generates synthetic events.

Below is the full flow of how data moves through the system:

```
fake_client/send_fake_events.py  
    → sends JSON POST requests →  
FastAPI /events endpoint  
    → validated by Pydantic (app/models.py) →  
Kafka producer (app/producer/kafka_producer.py)  
    → Kafka topic  
        → consumer_service/main.py  
            → processes events in real time
```



### Directory Structure
```
project/
│── config.py                       # kafka_conf + schema_registry_conf
│
│── app/
│   ├── main.py                     # FastAPI app, runs the server
│   ├── models.py                   # Pydantic models for request validation
│   ├── producer/
│   │    └── kafka_producer.py      # Functions to produce messages
│   └── routes/
│        └── producer_routes.py     # FastAPI endpoints (/events, /health)
│
│── consumer_service/
│   └── main.py                     # Kafka consumer (separate process)
│
│── schemas/
│   └── user_action_schema.json     # Kafka JSON schema
│
│── scripts/
│   └── create_topic.py             # Topic creation script
│
│── fake_client/
│   └── send_fake_events.py         # Generates fake events + posts to API
│
└── requirements.txt
```