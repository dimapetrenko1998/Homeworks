from fastapi import FastAPI, HTTPException, Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


templates = Jinja2Templates(directory="templates")


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


users = []


@app.get("/")
async def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int) -> User:
    user_id = len(users) + 1  # Генерация нового ID
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Создаем несколько пользователей
@app.on_event("startup")
async def startup_event():
    create_user("UrbanUser", 24),
    create_user("UrbanTest", 22),
    create_user("Capybara", 60),
