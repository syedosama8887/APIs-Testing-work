from fastapi import APIRouter

# Create a new router
router = APIRouter()

# Define the route handler for the second route
# @router.get("/hello_world_1")
# async def read_hello_world_1():
#     return {"message": "Hello, world 1!"}

# Define the route handler for the sum of two numbers
@router.get("/sum/{num1}/{num2}")
async def sum_numbers(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}

#subtract
@router.get("/subtract/{num1}/{num2}")
async def sum_numbers(num1: int, num2: int):
    result = num1 - num2
    return {"result": result}

@router.get("/multiplication/{num1}/{num2}")
async def sum_numbers(num1: int, num2: int):
    result = num1 * num2
    return {"result": result}

@router.get("/division/{num1}/{num2}")
async def sum_numbers(num1: int, num2: int):
    result = num1 / num2
    return {"result": result}
