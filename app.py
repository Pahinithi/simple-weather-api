from fastapi import FastAPI
import requests
from pydantic import BaseModel
from .settings import settings  

app = FastAPI()

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float

def get_weather(city: str):
    url = f"{settings.base_url}?q={city}&appid={settings.api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather_data
    else:
        return None

@app.get("/weather/{city}", response_model=WeatherResponse)
async def get_weather_endpoint(city: str):
    weather = get_weather(city)
    if weather:
        return weather
    else:
        return {"error": "City not found or API request failed"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)






