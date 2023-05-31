import telebot
from telebot import types


token = '5520340219:AAEGg-RH8fboT6ierDkSMXeAVUoWGTWH7AY'

bot = telebot.TeleBot(token)




admin_users = 478991565


#начальная страница
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('A')
    buttonB = types.KeyboardButton('B')
    buttonC = types.KeyboardButton('C')

    markup.row(buttonA, buttonB)
    markup.row(buttonC)

    bot.send_message(message.chat.id, 'It works!', reply_markup=markup)

if message.text == 'A':
    handle()


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(lambda call: True)
def handle(call):
    bot.send_message(chat_id=call.message.chat.id, message_id=call.message.id, text='It works!')
    bot.answer_callback_query(call.id)

    
    
    
    

bot.polling(none_stop=True, interval=0)