from pydantic import BaseModel

class posttype(BaseModel):
    title : str
    content :str
