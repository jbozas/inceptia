from app.services.external_services.base_api import BaseService
from app.schemas import CityLocation


class OpenWeatherMap(BaseService):
    BASE_URL = "https://api.openweathermap.org/data/2.5/"
    CHECK_TEMPERATURE = "weather?lat={lat}&lon={lon}&units=metric&appid=d81015613923e3e435231f2740d5610b"

    def is_hot_in_pehuajo(self) -> dict:
        url = self.BASE_URL + self.CHECK_TEMPERATURE.format(
            lat="-35.836948753554054", lon="-61.870523905384076"
        )
        return self._get(url)

    async def is_hot(
        self, temperature_limit: int = 28, city_location: CityLocation = None
    ) -> bool:
        """
        Checks if it's hot in a city received by param.
        If no city is received Pehuajo will be check it out.
        If no temperature_limit is received, 28 will be the limit to decide.

        Returns:
            bool: True if temperature is above temperature_limit degrees Celsius, False otherwise.
        """
        if city_location is None:
            temperature = self.is_hot_in_pehuajo()
        else:
            url = self.BASE_URL + self.CHECK_TEMPERATURE.format(
                lat=city_location.latitude, lon=city_location.longitude
            )
            temperature = self._get(url)
        temperature = temperature.get("main").get("temp", False)
        return temperature > temperature_limit if temperature else False
