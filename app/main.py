from fastapi import FastAPI
from app.database import Base, engine
from app.routers.users import router as users_router
from app.routers.jobs import router as jobs_router
from app.routers.favorites import router as favs_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(favs_router)
