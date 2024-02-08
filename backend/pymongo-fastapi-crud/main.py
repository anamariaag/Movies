from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router 
from fastapi.middleware.cors import CORSMiddleware

origins = [    
    "http://localhost:3000",
]

config = dotenv_values(".env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["url_connection"])
    app.database = app.mongodb_client[config["dbName"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    
    
app.include_router(router, tags=["movie"], prefix="/home")