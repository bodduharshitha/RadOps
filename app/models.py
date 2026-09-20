from pydantic import BaseModel


class SecurityEvent(BaseModel):
    type: str
    severity: str
    source: str
    description: str


class SecurityEventResponse(BaseModel):
    events: list[SecurityEvent]