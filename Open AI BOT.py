
import telebot
import random
import pyowm


privetstvie = ["!", "Шалом!", "Йоу!", "ХАИЛЬ", "Хэй", "Привет"]
how_are_you = ["Хочу пормереть", "На минус морали", "Умираю"]
good_bye = ["Увидимся", "Удачи", "Я умер!"]
what_is_your_name = ["Я бот Ануара"]

token ="891429087:AAF3OAGYxkc7j-2acAOVufu0AYyETwllYLE"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доступные команды: /weather /start')

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "Выберете город, что бы узнать погоду")
    bot.register_next_step_handler(city, weath)



def weath(message):
    owm = pyowm.OWM("891429087:AAF3OAGYxkc7j-2acAOVufu0AYyETwllYLE")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name)

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет" or message.text == "привет" or message.text == "Здравствуй" or message.text == "здравствуй" or message.text == "Йоу" or message.text == "йоу":
        bot.send_message(message.chat.id, random.choice(privetstvie) + ", " + message.chat.first_name)
    elif message.text == "Как дела?" or message.text == "как дела?" or message.text == "Как дела" or message.text == "как дела":
        bot.send_message(message.chat.id, random.choice(how_are_you))
    elif message.text == "Как тебя зовут?" or message.text == "как тебя зовут?" or message.text == "Как тебя зовут" or message.text == "как тебя зовут"
        bot.send_message(message.chat.id, random.choice(what_is_your_name))
    elif message.text == "Пока" or message.text == "пока"
        bot.send_message(message.chat.id, random.choice(good_bye))

if __name__ == "__main__":
    bot.polling(none_stop=True)
