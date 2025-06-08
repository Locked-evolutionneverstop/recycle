from telebot import TeleBot
from config import token
import os
import random

bot = TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот который может помочь тебе узнать как можно использовать разные виды отходов по типу стекла, пластика или пакетов. Также я могу рассказать о том, сколько разлагается определенной вид отходов!")

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    with open(f'images/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f, caption='Вот примеры как вы можете использовать пластик!')

@bot.message_handler(commands=['glass'])
def send_glass(message):
    img_name2 = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name2}', 'rb') as f:
        bot.send_photo(message.chat.id, f, caption='Вот примеры как вы можете использовать стекло!')

@bot.message_handler(commands=['plastic_bag'])
def send_plastic_bag(message):
    img_name3 = random.choice(os.listdir('images3'))
    with open(f'images3/{img_name3}', 'rb') as f:
        bot.send_photo(message.chat.id, f , caption='Вот примеры как вы можете использовать пластиковые пакеты!')

@bot.message_handler(commands=['plastic_time'])
def send_plastic_time(message):
    bot.reply_to(message, 'Привет! В среднем, пластиковые изделия могут разлагаться от 100 до 1000 лет. Например, обычные полиэтиленовые пакеты могут разлагаться от 100 до 400 лет, а пластиковые бутылки - от 100 до 450 лет. Более сложная пластиковая упаковка, такая как пакеты с застежкой "зип-лок" или упаковка HDPE, может разлагаться и до 1000 лет. ')


@bot.message_handler(commands=['glass_time'])
def send_glass_time(message):
    bot.reply_to(message, 'Привет! Стекло разлагается очень медленно, примерно за тысячу лет. Стекло не подвергается биологическому разложению, а постепенно разрушается на более мелкие частицы под воздействием природных факторов.')

@bot.message_handler(commands=['plastic_bag_time'])
def send_plastic_bag_time(message):
    bot.reply_to(message, 'Привет!Пластиковые пакеты разлагаются от 100 до 1000 лет, в зависимости от типа пластика и условий окружающей среды. Обычные полиэтиленовые пакеты разлагаются примерно за 100-200 лет, а пакеты с застежкой "зип-лок" могут разлагаться до 1000 лет. ')

bot.infinity_polling()






