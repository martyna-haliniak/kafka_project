### Provisional poroject structure

```
project/
│── config.py
│
│── app/
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   │    └── producer_routes.py
│   └── producer/
│        └── kafka_producer.py
│
│── consumer_service/
│   └── main.py
│
│── scripts/
│   └── create_topic.py         # topic creation
│
│── schemas/
│    └── user_action_schema.json
│
└── requirements.txt

```
