from pydantic import BaseModel

class CategoryCreateSchema(BaseModel):
    name: str
    

class CategoryGetSchema(BaseModel):
    id: int
    name: str | None = None


    
    
