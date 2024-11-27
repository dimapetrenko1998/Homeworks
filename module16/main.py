from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def main() -> dict:
    return {"messege": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"messege": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def id(
        user_id: int = Path(..., title="Enter User ID", ge=1, le=100)
) -> dict:
    return {"messege": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user(
        username: str = Path(..., title="Enter username", min_length=5, max_length=20),
        age: int = Path(..., title="Enter age", ge=18, le=120)
) -> dict:
    return {"messege": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
