from fastapi import FastAPI

app = FastAPI(title="API CI Lab")


@app.get("/")
def raiz():
    return {"status": "ok"}


@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a - b}
