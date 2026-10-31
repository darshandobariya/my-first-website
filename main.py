from fastapi import FastAPI

app = FastAPI(
    title="My First Website",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to my website!",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }