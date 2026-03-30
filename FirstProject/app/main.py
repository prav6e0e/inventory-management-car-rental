from fastapi import FastAPI
from core.config import settings
from database.db import engine, Base
from modules.User.router import router as UserRouter

# Table creation
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
)

app.include_router(UserRouter)

@app.get("/")
async def root():
    return {"message": "Hello World", "appName":settings.app_name,
            
            "docs":"/docs",
            
            
            }