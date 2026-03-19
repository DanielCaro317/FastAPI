from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel): 
    name: str
    cost: float
    in_stock: bool
    

products = []

# todo pull products
@app.get("/products")
def pull_products(): 
    return {"products": products}
 
# Add product
@app.post("/products")
def add_products(product: Product):
    products.append(product)
    return {"message": "Product added", "product": product}

#  Update product
@app.put("/products/{id}")
def update_product(id: int, product: str):
    products[id] = product
    return {"message": "Updated Product", "product": product}

#  Delete product
@app.delete("/products/{id}")
def delete_product(id: int): 
    deleted = products.pop(id)
    return {"message": "Product deleted", "product": deleted}

