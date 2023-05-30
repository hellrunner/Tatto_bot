import telebot
from telebot import types
from auth_data import token


bot = telebot.TeleBot(token)






@bot.message_handler(commands=['start'])
def start(message):
    
    name_user = message.from_user.first_name
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    group = types.KeyboardButton('Группа')
    start = types.KeyboardButton('asd')
    
    markup.add(group, start)
    bot.send_message(message.chat.id, f"""Привет, {name_user}, добро пожаловать в мой 
телеграм бот, здесь ты можешь""",reply_markup=markup)
    



# @bot.message_handler(commands=['group'])
# def group(message):
    
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("поcестить группу", url = "https://t.me/raznyikolkyi"))
    
#     bot.send_message(message.chat.id, "перейдите", reply_markup=markup)


# @bot.message_handler(commands=['help'])
# def group(message):
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
#     group = types.KeyboardButton('Группа')
#     start = types.KeyboardButton('Start')
    
#     markup.add(group, start)
    
    
#     bot.send_message(message.chat.id, "перейдите", reply_markup=markup)


bot.polling(none_stop=True)