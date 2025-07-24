from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from blog import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def destroy(id, db: Session):
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first().title
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id \'{id}\' not found!")
    
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()

    return {'message': f"Blog {blog} sucessfuly deleted."}

def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id \'{id}\' not found!")
    
    blog.update(request)
    db.commit()

    return 'updated succesfully'

def show(id: int, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with the id \'{id}\' is not available.") # aviso caso não encontre o blog
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"Blog with the id \'{id}\' is not available."}
        
    return blog