from fastapi import FastAPI, HTTPException
from .models import Category
from .schemas import CategoryCreateSchema, CategoryGetSchema
from .dependencies import db_dependency
app = FastAPI()


# Create category

@app.post("/categories/create", response_model=CategoryGetSchema)
def create_category(category: CategoryCreateSchema, db:db_dependency):
    new_category = Category(**category.model_dump(exclude_unset=True))
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# get all category
@app.get("/categories", response_model=list[CategoryGetSchema])
def get_categories(db: db_dependency):
    return db.query(Category).all()

# get one category by id
@app.get("/category-single/{category_id}", response_model=CategoryGetSchema, status_code=200)
def get_category(category_id: int, db: db_dependency):
    c = db.query(Category).filter(Category.id == category_id)
    if c.first() is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    print(c, "###########################################################")
    return c.first()

# Update Category

@app.put("/categories/{category_id}", response_model=CategoryGetSchema, status_code=200)
def update_category(category_id: int, category: CategoryCreateSchema, db: db_dependency):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category



# Delete Category
@app.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: int, db: db_dependency):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return None






# @app.get("/hello")   # 127.0.0.1:8000/hello
# def hello():
    
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")    #item_id >>> path argument
# def read_item(item_id: int, category: str = None):
#     return {"item_id": item_id, "category": category}




