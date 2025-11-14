from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return {
        "mensaje": "Servicio de usuarios funcionando con su propia base de datos"
    }

@app.get("/")
def root():
    return {
        "mensaje": "Servicio de usuarios funcionando con su propia base de datos"
    }