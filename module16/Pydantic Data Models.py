from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()


templates = Jinja2Templates(directory="templates")


users = []



class User(BaseModel):
    id: int
    username: str
    age: int



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users", response_model=List[User])
def get_users():
    return users



@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")



@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user



@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")



@app.on_event("startup")
def startup_event():
    create_user("UrbanUser", 24)
    create_user("UrbanTest", 22)
    create_user("Capybara", 60)
