### Provisional poroject structure

```
project/
│── config.py                   # kafka_conf + schema_registry_conf
│
│── app/
│   ├── main.py                 # FastAPI app, runs the server
│   ├── models.py               # Pydantic models for request validation
│   ├── producer/
│   │    └── kafka_producer.py  # Functions to produce messages
│   └── routes/
│        └── producer_routes.py # FastAPI endpoints
│
│── consumer_service/
│   └── main.py                 # Kafka consumer (separate process)
│
│── schemas/
│   └── user_action_schema.json # Kafka JSON schema
│
│── scripts/
│   └── create_topic.py         # Topic creation
│
└── requirements.txt


```
