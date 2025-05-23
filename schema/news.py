from pydantic import BaseModel

class CreateNews(BaseModel):
    text : int

class UpdateNews(BaseModel):
    text : int