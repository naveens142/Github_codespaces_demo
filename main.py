from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message","Home Page"}

@app.get("/health")
def health():
    return {"message", "Health is good."}