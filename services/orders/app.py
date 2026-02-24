from fastapi import FastAPI
import os

if not os.getenv("DB_PASSWORD"):
    raise Exception("Database password not set")

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
