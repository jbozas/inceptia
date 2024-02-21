import logging

from fastapi import HTTPException, status, APIRouter

from app.services.stock_service import StockChecker
from app.schemas import CheckTemperature, Product
from app.services.external_services.weather import OpenWeatherMap

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/check_temperature",
    status_code=status.HTTP_200_OK,
    description="Checks that the temperature of a Location don't exceed the limit.",
)
async def is_hot(payload: CheckTemperature = CheckTemperature()):
    logger.info("Checking temperature.")
    is_hot: bool = await OpenWeatherMap().is_hot(
        payload.temperature_limit, payload.city_location
    )

    return "Bienvenida 1" if is_hot else "Bienvenida 2"


@router.get(
    "/is_product_available",
    status_code=status.HTTP_200_OK,
    description="Checks that product's stock exists.",
)
async def has_stock(product: Product):
    logger.info(f"Checking stock for {product.product_name}.")
    try:

        has_stock: bool = await StockChecker().is_product_available(product)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Too many request for the same product. Try later.",
        )
    return "Hay Stock!" if has_stock else "No hay Stock!"
