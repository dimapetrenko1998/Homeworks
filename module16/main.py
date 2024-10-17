from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main() -> dict:
    return {"messege": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"messege": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def id(user_id: int) -> dict:
    return {"messege": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/")
async def user(usermane: str, age: int) -> dict:
    return {"messege": f"Информация о пользователе. Имя: {usermane}, Возраст: {age}"}