from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

def get_all(db: Session):
    users = db.query(models.User).all()
    
    return users

def show(id: int, response: Response, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User with the id \'{id}\' is not available.") # aviso caso não encontre o user
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"User with the id \'{id}\' is not available."}
        
    return user