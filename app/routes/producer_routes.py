from fastapi import APIRouter
from app.models import UserAction
from app.producer.kafka_producer import produce_event

router = APIRouter()

@router.post("/events")
def send_event(event: UserAction):
    """
    Receives event from client, sends to Kafka.
    """
    produce_event(event.dict())  # convert Pydantic model to dict
    return {"message": "Event sent successfully"}

@router.get("/health")
def health_check():
    return {"status": "ok"}