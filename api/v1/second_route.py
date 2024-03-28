from fastapi import APIRouter

# Create a new router
router = APIRouter()

# Define the route handler for the second route
@router.get("/hello_world_2")
async def read_hello_world_2():
    return {"message": "Hello, world 2!"}


