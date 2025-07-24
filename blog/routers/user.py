from typing import List
from fastapi import APIRouter, Depends, Response, status
from blog import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags= ['User']
)

@router.post('/')
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)
    

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return user.show(id, response, db)