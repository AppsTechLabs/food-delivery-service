from fastapi import FastAPI, Depends,status,HTTPException, Request

from fastapi.responses import HTMLResponse

from auth import auth_router,get_current_user

from typing import Annotated

from order import order_router 

from items import items_router

from  database import engine,SessionLocal

import models

from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session

app=FastAPI()

app.include_router(auth_router)

app.include_router(order_router)

app.include_router(items_router)


models.Base.metadata.create_all(bind=engine)

app.mount("/Templates", StaticFiles(directory="Templates"), name="Templates")

template=Jinja2Templates(directory="Templates")

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]

@app.get('/', response_class=HTMLResponse)
async def user(request:Request):

    return template.TemplateResponse("form.html", {"request":request})
    
    # if user is None:

    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    
    # return {'User':user}



