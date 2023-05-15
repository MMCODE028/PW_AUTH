from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv
import urllib3
import warnings
warnings.filterwarnings('ignore')

urllib3.disable_warnings()

# os.environ['REQUESTS_CA_BUNDLE'] = r'\\ht5ry23\\COMPARTIDO\\USUARIOS\\AMX\\Fortinet_CA_SSL .cer' # Wokraround Ghenova Firewall

# Cargando las variables de entorno 

Forge_CLIENT_ID = os.getenv('Forge_CLIENT_ID')
Forge_CLIENT_SECRET = os.getenv('Forge_CLIENT_SECRET')



authForge_router = APIRouter()

@authForge_router.get("/token")
def AuthToken():
    # Requerimientos 
        # Cliente ID
        # Secret ID
        # Grant_type [Permisos]

    url = "https://developer.api.autodesk.com/authentication/v1/authenticate"
    payload='grant_type=client_credentials&client_id=E80hYNGC3AQrEQotFe4HI3t1djRc3XDC&client_secret=GQpAFduVO6ciiEDe&scope=data%3Aread%20data%3Awrite%20data%3Acreate%20bucket%3Aread%20bucket%3Acreate'
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['access_token'] 
    return {"access_token":token}



