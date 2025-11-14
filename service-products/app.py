from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products():
    return {"mensaje": "Servicio de productos funcionando con su propia base de datos"}

@app.get("/")
def root():
    return {"mensaje": "Servicio de productos funcionando con su propia base de datos"}
