from fastapi import FastAPI

app = FastAPI(title="Synthetic Cognitive System V0.1")


@app.get("/")
def home():
    return {
        "system": "Synthetic Cognitive System",
        "version": "V0.1",
        "status": "online"
    }