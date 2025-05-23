from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.users import Users
from routers.login import get_current_user
from schema.news import UpdateNews,CreateNews
from models.news import News
from functions.news import news_post,news_put,news_delete
from db import database

routers_news = APIRouter(tags=["Yangiliklar"])


@routers_news.get('/get_news')
def news_kurish(db: Session = Depends(database)):
    return db.query(News).all()


@routers_news.post('/post_news')
def news_qushish(form: CreateNews,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_user)):
    return news_post(form,db,current_user)



@routers_news.put('/put_news')
def news_yangilash(ident: int, form: UpdateNews,db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return news_put(ident,form,db,current_user)


@routers_news.delete('/delete_news')
def news_uchirish(ident: int,db: Session = Depends(database),
                  current_user: Users = Depends(get_current_user)):
    return news_delete(ident,db,current_user)