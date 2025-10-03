import random
from enum import Enum

from pydantic import BaseModel, Field

def generate_tracking_number():
    return random.randint(100000,999999)


# Generate uuid number
def generate_uuid():
    import uuid
    return str(uuid.uuid4())

class ShipmentStatus(str,Enum):
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"

class Shipment(BaseModel):
    uid: str = Field(default_factory=generate_uuid)
    order_id: int = Field(lt=10)
    shipped_date: str
    delivery_date: str
    status: str = Field(default = ShipmentStatus.PENDING)
    tracking_number: str = Field(default_factory=generate_tracking_number)