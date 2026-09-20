from fastapi import FastAPI

from app.models import SecurityEvent, SecurityEventResponse

app = FastAPI(title="RadOps")


@app.get("/")
def root():
    return {
        "project": "RadOps",
        "message": "RadOps API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/security-events", response_model=SecurityEventResponse)
def security_events():
    return {
        "events": [
            SecurityEvent(
                type="LOGIN_FAILURE",
                severity="MEDIUM",
                source="10.0.0.15",
                description="Multiple failed login attempts"
            ),
            SecurityEvent(
                type="SUSPICIOUS_TRAFFIC",
                severity="HIGH",
                source="10.0.0.99",
                description="Unusually high request rate detected"
            )
        ]
    }

@app.post("/api/security-events", response_model=SecurityEvent)
def create_security_event(event: SecurityEvent):
    return event