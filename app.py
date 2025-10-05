from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def healthy():
    return {"status": "healthy"}
