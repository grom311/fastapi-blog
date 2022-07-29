from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas
from db.service import get_db
from repository import user_core

router = APIRouter(
    prefix="/user",
    tags=['User'],
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_core.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_core.get_user(id, db)
