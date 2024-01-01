# Reference
# https://pypi.org/project/open-meteo/

import asyncio

from open_meteo import OpenMeteo
from open_meteo.models import DailyParameters, HourlyParameters


async def main():
    """Show example on using the Open-Meteo API client."""
    async with OpenMeteo() as open_meteo:
        forecast = await open_meteo.forecast(
            latitude=35.0,
            longitude=150.0,
            current_weather=True,
            daily=[
                DailyParameters.SUNRISE,
                DailyParameters.SUNSET,
            ],
            hourly=[
                HourlyParameters.TEMPERATURE_2M,
                HourlyParameters.RELATIVE_HUMIDITY_2M,
            ],
        )
        print(forecast)


if __name__ == "__main__":
    asyncio.run(main())
