from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router as item_routes
from app.comments.routes import router as comment_routes  

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API con FastAPI")

app.include_router(item_routes)       # Para /items
app.include_router(comment_routes)    # Para /comments
