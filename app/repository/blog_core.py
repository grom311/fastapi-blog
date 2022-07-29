from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas


def get_all(db: Session):
    query = db.query(models.Blog).all()
    return query

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    query = db.query(models.Blog).filter(models.Blog.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} not found.')
    query.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Blog, db: Session):
    query = db.query(models.Blog).filter(models.Blog.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog {id} not found.')
    query.update({'title':request.title, 'body': request.body})
    db.commit()
    return f"post {id} updatetd"

def get_blog(id: int, db: Session):
    query = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not allowed.")
    return query
