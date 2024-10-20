from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..backend.db_depends import get_db
from typing import Annotated
from ..models import user
from ..schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix='/task', tags=['task'])


@router.get("/", response_model=list[user])
def all_s(db: Annotated[Session, Depends(get_db)]):
    users = db.execute(select(user)).scalars().all()
    return users


#### Функция для получения пользователя по ID
@router.get("/{user_id}", response_model=user)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = user(**user.dict())
    db.execute(insert(user).values(new_user))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


#### Функция для обновления пользователя
@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(update(user).where(user.id == user_id).values(**user.dict()))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


#### Функция для удаления пользователя
@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(user).where(user.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'User deleted successfully!'}


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('/delete')
async def delete_task():
    pass
