from fastapi import FastAPI

from routers.user.router import router as user_router
from routers.product.router import router as product_router
from routers.comment.router import router as comment_router
from routers.personal.router import router as personal_router
from routers.offer.router import router as offer_router

app = FastAPI()

app.include_router(user_router, tags=['users'])
app.include_router(product_router, tags=['product'])
app.include_router(comment_router, tags=['comment'])
app.include_router(personal_router, tags=['personal'])
app.include_router(offer_router, tags=['offer'])
