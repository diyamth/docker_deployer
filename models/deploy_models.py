from pydantic import BaseModel
from typing import Optional

# Request schema for deployment
class DeployRequest(BaseModel):
    container_name: str
    image_name: str
    env_vars: Optional[dict] = None
    use_gpu: Optional[bool] = False

# Response schema for success/failure
class DeployResponse(BaseModel):
    success: bool
    message: str

# Request schema for stopping a container
class StopRequest(BaseModel):
    container_name: str

# Logs fetching query parameters
class LogsResponse(BaseModel):
    success: bool
    logs: Optional[str] = None
    message: Optional[str] = None

# Status checking
class StatusResponse(BaseModel):
    success: bool
    is_running: bool
    message: Optional[str] = None
