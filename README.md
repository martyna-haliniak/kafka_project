# Real-Time Event Streaming Pipeline (FastAPI + Kafka)

This project simulates a real-time data pipeline using **FastAPI**, **Kafka**, **Schema Registry**, and a **mock client** that generates synthetic events.
It demonstrates API design, event validation, Kafka streaming, and real-time consumption.

---
## System Architecture 

```java
fake_client/send_fake_events.py  
    → POST /events  
FastAPI API (producer_routes.py)  
    → Pydantic validation (UserAction)  
    → Kafka Producer (kafka_producer.py)  
        → Kafka Topic ("events")  
            → Kafka Consumer (consumer_service/)
```
---

## Data Lifecycle
**Step-by-step**

**1. Fake Client generates an event**
→ random JSON user activity
→ sent via POST http://127.0.0.1:8000/events

**2. FastAPI receives the request**
→ matches /events endpoint
→ parses JSON into a UserAction Pydantic model

**3. Producer sends event to Kafka**
→ validated
→ serialized using Schema Registry
→ written to Kafka topic events

**4. Kafka stores the event**
→ retained until consumed
→ FastAPI stays stateless

**5. Kafka Consumer**
→ reads events
→ processes or aggregates them in real-time

---


## Visual Flow (simple)
```arduino
Fake Client
    ↓ POST /events
FastAPI Router
    ↓ validates UserAction
Kafka Producer
    ↓
Kafka Topic: "events"
    ↓
Consumer
```
---

## Directory Structure
```
project/
│── config.py                       # kafka_conf + schema_registry_conf
│
│── app/
│   ├── main.py                     # FastAPI app, runs the server
│   ├── models.py                   # Pydantic models for request validation
│   ├── producer/
│   │     └── kafka_producer.py     # Functions to produce messages
│   └── routes/
│         └── producer_routes.py    # FastAPI endpoints (/events, /health)
│
│── consumer_service/
│   ├── standard_consumer.py        # Standard Kafka consumer 
│   └── faust_consumer.py           # Faust consumer
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




---


## /health
Can be improved.
Try:
```python
@app.get("/health")
def health_check():
    try:
        # try to ping Kafka
        producer = Producer(kafka_conf)
        producer.list_topics(timeout=1)
        return {"status": "ok", "kafka": "ok"}
    except:
        return {"status": "degraded", "kafka": "unreachable"}
```
---

## Running the project:
### 1. Install dependencies
`pip install -r requirements.txt`

### 2. Start the API
`uvicorn app.main:app --reload`

### 3. Start fake client in a separate terminal
`python fake_client/send_fake_events.py`

### 4. Start consumer in a separate terminal
`python -m consumer_service.main`

