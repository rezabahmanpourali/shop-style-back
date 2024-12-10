from fastapi import FastAPI
from src.category.routes import category_router
from src.product.routes import product_router
from src.auth.routes import auth_router
from src.banners.routes import banner_router
app = FastAPI()

app.include_router(banner_router, prefix="/banners", tags=["Banners"])
app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(category_router, prefix="/categories", tags=["Categories"])
app.include_router(product_router, prefix="/products", tags=["Products"])