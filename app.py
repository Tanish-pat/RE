from fastapi import FastAPI
from pydantic import BaseModel
from model_predictor import ModelPredictor
import threading
import time
import os
import signal

app = FastAPI()
predictor = ModelPredictor()

# Define the request body schema
class MessageRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Spam detection API"}

@app.post("/predict")
def predict(request: MessageRequest):
    prediction = predictor.predict(request.message)
    return {"prediction": prediction}

# Shutdown the server after 5 seconds
def shutdown_after_delay(delay: int):
    time.sleep(delay)
    # Send a termination signal to the process
    os.kill(os.getpid(), signal.SIGINT)

# Start the shutdown timer in a background thread
if __name__ == "__main__":
    threading.Thread(target=shutdown_after_delay, args=(5,), daemon=True).start()
