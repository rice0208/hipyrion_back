from fastapi.middleware.cors import CORSMiddleware
from .user import user_router
from .post import post_router
from . import app

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(post_router)


@app.get("/")
def index():
    return {"Hipyrion": "Welcome to Hipyrion's web api!"}
