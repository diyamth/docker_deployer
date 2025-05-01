from fastapi import FastAPI
from app.api.container_ops import router as container_router

# Create a FastAPI application instance
app = FastAPI()

# Include the container operations API router
app.include_router(container_router)


	
