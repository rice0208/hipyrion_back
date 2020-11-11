from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .user import user_router
from .post import post_router

app = FastAPI()
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True)
