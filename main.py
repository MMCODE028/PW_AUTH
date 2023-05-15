import uvicorn
from fastapi import FastAPI
from Auth import authForge_router
from fastapi.middleware.cors import CORSMiddleware
import os

# os.environ['REQUESTS_CA_BUNDLE'] = r'\\ht5ry23\\COMPARTIDO\\USUARIOS\\AMX\\Fortinet_CA_SSL .cer' # Wokraround Ghenova Firewall


app = FastAPI()
app.title = 'API_POWERBI'
app.version = "V1"



app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(authForge_router, prefix='/authv1', tags=["Autentificacion"])

@app.get('/', tags=["Inicio"])
def message():
    return {"Mensaje": "Bienvenido a la API AUTH-FORGE"}





