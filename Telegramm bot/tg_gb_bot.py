import telebot
from random import *
import json

films = []


def save():
    with open("films.Json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("FilmBase saved successfully in Films.json")


def load():
    global films
    with open("films.Json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("FilmBase loaded successfully.")


API_TOKEN = '5506595477:AAG-766IIUsIphtx99_hhcolS1QA8gaPzAg'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Filmbase is loaded successfilly")
    except:
        films.append("Maxtix")
        films.append("Sollaris")
        films.append("Lord of the Rings")
        films.append("Chainsaw from Texxas")
        films.append("Santa Barbara")
        bot.send_message(message.chat.id, "Filmbase is loaded successfilly as default")


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, "Film list: ")
    bot.send_message(message.chat.id, ",".join(films))


bot.polling()
