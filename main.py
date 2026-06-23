from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message","This is Home Page, modify by codespave"}

@app.get("/health")
def health():
    return {"message", "Health is good."}