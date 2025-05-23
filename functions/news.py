from http.client import HTTPException
from models.news import News


def news_post(form,db,current_user):
    if current_user.role == 'admin':
        new = News(
            text = form.text
        )
        db.add(new)
        db.commit()
        return {"Message": "News qushildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


def news_put(ident,form,db,current_user):
    if current_user.role == 'admin':
        db.query(News).filter(News.id == ident).update({
            News.text : form.text
        })
        db.commit()
        return {"Message": "News yangilandi !!! "}
    else:
        raise HTTPException(404, "Siz admin emasz !!! ")


def news_delete(ident,db,current_user):
    if current_user.role == 'admin':
        db.query(News).filter(News.id == ident).delete()
        db.commit()
        return {"Message": "News uchirlidi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")

