import telebot
import config
import trueList
import actionList
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Правда🔥', 'Дія😺', 'FAQ❓')
    bot.send_message(message.chat.id, 'Привітик!👋 \n Я бот для гри у один із найпопулярніших у світі патігеймів "Правда чи дія"🎉. \n Для того щоб почати використання клацни на кнопку внизу!✅', reply_markup=user_markup)


@bot.message_handler(commands=['true', 'правда'])
def true_command(message):
    trueQuestion = random.randint(0, len(trueList.true))
    bot.send_message(message.chat.id, trueList.true[trueQuestion-1])
@bot.message_handler(commands=['action', 'Дія', 'дія'])
def action_command(message):
    actionQuestion = random.randint(0, len(actionList.act))
    bot.send_message(message.chat.id, actionList.act[actionQuestion-1])

bot.polling(none_stop=True)