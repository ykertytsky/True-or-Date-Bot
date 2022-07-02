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

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == 'Правда🔥' or 'правда' or 'Правда':
        trueQuestion = random.randint(0, len(trueList.true))
        bot.send_message(message.chat.id, trueList.true[trueQuestion-1])
    elif message.text == 'Дія😺' or 'Дія' or 'дія':
        actionQuestion = random.randint(0, len(actionList.act))
        bot.send_message(message.chat.id, actionList.act[actionQuestion-1])
    elif message.text == 'FAQ❓':
        bot.send_message(message.chat.id, 'Test')
    else:
        bot.send_message(message.chat.id, 'Вибачте, я вас не зрозумів😿')

@bot.message_handler(commands=['true', 'правда'])
def true_command(message):
    trueQuestion = random.randint(0, len(trueList.true))
    bot.send_message(message.chat.id, trueList.true[trueQuestion-1])

bot.polling(none_stop=True)