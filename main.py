from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.wallet_routes import router as wallet_router
from database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(wallet_router, prefix="/wallet", tags=["wallet"])
