import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Replace with your actual bot token and OpenWeatherMap API key
BOT_TOKEN = "5516819203:AAF1StoymYUSZpKK5rZOdx0Q4cEClRjA5S4"
WEATHER_API_KEY = "86ab45fddd737d284931f408174fc407"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Function to get weather data
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Function to provide clothing recommendations based on temperature
def clothing_recommendation(temp):
    if temp < 0:
        return "It's freezing! Wear a heavy coat, gloves, and a hat."
    elif 0 <= temp < 10:
        return "It's cold outside. Wear a warm jacket and a scarf."
    elif 10 <= temp < 20:
        return "It's cool. A light jacket or sweater should be fine."
    elif 20 <= temp < 30:
        return "The weather is warm. Wear light clothing."
    else:
        return "It's hot! Wear shorts and a t-shirt, and stay hydrated."

@dp.message()
async def get_forecast(message: Message):
    city = message.text.strip()
    weather_data = get_weather(city)
    if weather_data:
        temp = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        recommendation = clothing_recommendation(temp)
        
        await message.answer(
            f"The current temperature in {city} is {round(temp)}°C with {weather_desc}.\n{recommendation}"
        )
    else:
        await message.answer("Sorry, I couldn't fetch the weather for that location. Please check the city name and try again.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(main())
