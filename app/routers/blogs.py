from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas
from db.service import get_db
from repository import blog_core
from blog import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['Blogs'],
    dependencies=[Depends(oauth2.get_current_user)],
)


@router.get('/', response_model=List[schemas.ShowBlog])
async def all(db: Session = Depends(get_db)):
    return blog_core.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_core.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    return blog_core.get_blog(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog_core.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_core.update(id, request, db)
