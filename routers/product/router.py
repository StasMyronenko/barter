from fastapi import APIRouter

from schemes.product.schema import ProductCreateSchema, ProductUpdateSchema
from services.product.ProductService import ProductService

router = APIRouter(prefix="/product")


@router.post("/create")
async def create_product(product: ProductCreateSchema):
    ProductService.create(
        product.owner_id,
        product.description,
        product.title,
        product.image_url,
    )
    return {"status": "created"}


@router.get("/all")
async def read_all_products():
    users = ProductService.read_all()
    return {"products": users}


@router.get("/{product_id}")
async def read_product_by_id(product_id: int):
    product = ProductService.read_by_id(product_id)
    return {"product": product}


@router.post("/update")
async def update_product_by_id(product: ProductUpdateSchema):
    print(product)
    ProductService.update_by_id(
        product.id,
        product.new_owner_id,
        product.new_description,
        product.new_title,
        product.new_image_url,
    )
    return {"status": "updated"}


@router.delete("/delete/{user_id}")
async def delete_product(user_id: int):
    ProductService.delete_by_id(user_id)
    return {"status": "deleted"}
