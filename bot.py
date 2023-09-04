import telebot
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

token = '5520340219:AAEGg-RH8fboT6ierDkSMXeAVUoWGTWH7AY'

bot = telebot.TeleBot(token)

admin_users = [478991566]

maybe =""
zapis_k_sashe = ""



#начальная страница
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋")
    btn2 = types.KeyboardButton("я admin")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "👋 Привет! Я бот-помошник!", reply_markup=markup)


@bot.message_handler(commands=['calendar'])
def calendar(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,f"Select {LSTEP[step]}",reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",c.message.chat.id,c.message.message_id,reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",c.message.chat.id, c.message.message_id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if '👋' in  message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) #создание новых кнопок
        
        zapis = types.KeyboardButton('Запись')
        rtyu = types.KeyboardButton('Календарь записей')
        chanal = types.KeyboardButton('Канал')
        back = types.KeyboardButton('Вернутся')
        markup.add(zapis, rtyu, chanal, back)
        bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=markup) #ответ бота
    
    elif message.text == 'Вернутся':
        start(message)

    elif message.text == 'кто я?':
        user_id = message.from_user.id
        bot.send_message(message.from_user.id, f'ваш айди {user_id}', parse_mode='Markdown')

    elif message.text == 'Запись':
        bot.send_message(message.from_user.id, 'Если хотите записаться, то начните сообщение со слов "хочу запись"', parse_mode='Markdown')

    elif message.text == 'Канал':
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text='тыкать сюды', url='https://t.me/raznyikolkyi')
        markup.add(btn5)
        bot.send_message(message.from_user.id, "мой канал", reply_markup = markup)

    elif message.text == 'я admin':
        if message.from_user.id in admin_users:
            get_mess_from_admin(message)   
        else: bot.send_message(message.from_user.id, "к сожалению вы не админ")
    elif message.text == '666':
        admin_users.append(message.from_user.id)
        bot.send_message(message.from_user.id, "У вас появился доступ к админке")
    
    elif message.text == 'Календарь записей':
        calendar(message)
    
    
    elif "хочу запись" in message.text or "Хочу запись" in message.text:
        global zapis_k_sashe
        global maybe
        maybe = f"{zapis_k_sashe} \n @{message.from_user.username} \n {message.text}"
        get_mess_from_zakas(message)
    
    elif message.text =="да, отправить":
        zapis_k_sashe = maybe
        bot.send_message(message.from_user.id, f"Ваша запись успешно отправленна мастеру")
        start(message)
    
    elif message.text == "Посмотреть записи":
        bot.send_message(message.from_user.id, f"Все записи: {zapis_k_sashe}")
    elif message.text == "Очистить записи":
        zapis_k_sashe = ""
        bot.send_message(message.from_user.id, f"Ваши записи успешно очищены")




def get_mess_from_admin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    why = types.KeyboardButton('Посмотреть записи')
    who = types.KeyboardButton('Календарь записей')
    backk = types.KeyboardButton('Вернутся')
    clear_zap = types.KeyboardButton('Очистить записи')
    markup.add(why,who,backk, clear_zap)
    bot.send_message(message.from_user.id, 'привет, хозяин', reply_markup = markup)
            
def get_mess_from_zakas(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    yes_zakas = types.KeyboardButton('да, отправить')
    no_zakas = types.KeyboardButton('нет, не отправлять👋')
    markup.add(yes_zakas, no_zakas)
    bot.send_message(message.from_user.id, f"Вы уверенны, что хотите иметь запись на сеанс с такими пожеланиями? \n{message.text}", reply_markup= markup)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)