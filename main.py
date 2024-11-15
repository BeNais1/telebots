import telebot
import requests
import time

# Токен вашего бота (получить у BotFather)
bot_token = '7893269380:AAFVSViN_Pu-bqT7u7lWHGSs-ie557BqSgw'

# ID вашего канала
chat_id = '-1002358751007'

# Базовый URL для получения цены Bitcoin с Binance
base_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

# Инициализация бота
bot = telebot.TeleBot(token=bot_token)

def get_btc_price():
    response = requests.get(base_url)
    data = response.json()
    return data['price']

while True:
    try:
        price = get_btc_price()
        message = f"BTC/USDT ~ {price}"
        bot.send_message(chat_id, message)
        time.sleep(30)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(30)