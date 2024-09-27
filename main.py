from fastapi import FastAPI
from db import Base, engine, get_db
from routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router=router, prefix="/items", tags=["items"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


