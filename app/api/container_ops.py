from fastapi import APIRouter, HTTPException
from services.docker_deployer import DockerDeployer
from models.deploy_models import DeployRequest

# Initialize FastAPI router
router = APIRouter()

# Create an instance of DockerDeployer to manage container operations remotely
deployer = DockerDeployer(
    hostname=os.getenv("SSH_HOSTNAME"),
    username=os.getenv("SSH_USERNAME"),
    private_key_path=os.getenv("PRIVATE_KEY_PATH")
)

@router.post("/deploy")
async def deploy_container(request: DeployRequest):
    """
    Deploy a new container with the specified configuration.
    """
    await deployer.deploy_container(
        container_name=request.container_name,
        image_name=request.image_name,
        env_vars=request.env_vars,
        use_gpu=request.use_gpu
    )
    return {"status": "success"}

@router.post("/container/{container_name}/start")
async def start_container(container_name: str):
    """
    Start a specific container by name.
    """
    try:
        await deployer.start_container(container_name)
        return {"status": "success", "message": f"Container '{container_name}' started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/container/{container_name}/stop")
async def stop_container(container_name: str):
    """
    Stop a specific container by name.
    """
    try:
        await deployer.stop_container(container_name)
        return {"status": "success", "message": f"Container '{container_name}' stopped."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/container/{container_name}/restart")
async def restart_container(container_name: str):
    """
    Restart a specific container by name.
    """
    try:
        await deployer.restart_container(container_name)
        return {"status": "success", "message": f"Container '{container_name}' restarted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/container/{container_name}")
async def delete_container(container_name: str):
    """
    Delete a specific container by name.
    """
    try:
        await deployer.delete_container(container_name)
        return {"status": "success", "message": f"Container '{container_name}' deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

