from fastapi import FastAPI

user_db=[
    {"user": "admin", "pass": "admin123"},
    {"user": "usuario1", "pass": "pass123"},
    {"user": "test", "pass": "test123"}
]
app=FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.post("/login")
def login(username: str, password: str):
    for usuario in user_db:
        if usuario["user"] == username and usuario["pass"] == password:
            return {"status": "ok", "message": "Login correcto"}
    
    return {"status": "error", "message": "Usuario o contraseña incorrectos"}

@app.get("/")
def inicio():
    return {"message": "API Login Simple - POST a /login con username y password"}