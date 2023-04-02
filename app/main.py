from fastapi import FastAPI
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


# with alembic, we no longer need sqlalchemy to create tables and columns
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "S.a World"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# dependency hell enjoyer
