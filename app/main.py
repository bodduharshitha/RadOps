from fastapi import FastAPI

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