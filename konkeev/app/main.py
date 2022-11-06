from fastapi import FastAPI

from routes.views import router

app = FastAPI()
app.include_router(
    router
)



