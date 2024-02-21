from pydantic import BaseModel


class CityLocation(BaseModel):
    latitude: str = None
    longitude: str = None


class CheckTemperature(BaseModel):
    temperature_limit: int = 28
    city_location: CityLocation = None


class Product(BaseModel):
    product_name: str = ...
    quantity: int = ...
