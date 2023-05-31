import telebot
from telebot import types


token = '5520340219:AAEGg-RH8fboT6ierDkSMXeAVUoWGTWH7AY'

bot = telebot.TeleBot(token)




admin_users = 478991565


#начальная страница
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋")
    btn2 = types.KeyboardButton("я admin")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Я бот-помошник!", reply_markup=markup)





@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) #создание новых кнопок
        btn1 = types.KeyboardButton('кто я?')
        btn2 = types.KeyboardButton('Правила')
        btn3 = types.KeyboardButton('че')
        btn4 = types.KeyboardButton('вернутся')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=markup) #ответ бота


    elif message.text == 'кто я?':
        user_id = message.from_user.id
        bot.send_message(message.from_user.id, f'ваш айди {user_id}', parse_mode='Markdown')

    elif message.text == 'Правила':
        bot.send_message(message.from_user.id, 'нету правил', parse_mode='Markdown')

    elif message.text == 'че':
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
        markup.add(btn5)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)

    elif message.text == 'вернутся':
        start(message)
    
    elif message.text == 'я admin':
        #bot.register_next_step_handler(message, get_mess_from_admin)
        get_mess_from_admin(message)
    
    
    
    
    
    
    
    
    
def get_mess_from_admin(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('почему я')
    btn2 = types.KeyboardButton('почему ns')
    btn3 = types.KeyboardButton('вернутся')
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.from_user.id, 'привет', reply_markup = markup)
        
    if message.text == 'вернутся':
        start(message)
        
bot.polling(none_stop=True, interval=0)