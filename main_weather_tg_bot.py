import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])


        await message.reply(f'Погода в городе: {city}\nТемпература: {cur_weather} C\n' 
              f'Влажность: {humidity}%\nВетер: {wind}м/c\n'
              f'Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}\n'
              f'Хорошего дня'
              )

    except:
        await message.reply('Проверте название города')








if __name__ == '__main__':
    executor.start_polling(dp)