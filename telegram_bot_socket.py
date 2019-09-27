import telebot
from telebot import types



bot = telebot.TeleBot(token)
configurations = {}
freq=['11785', '11900', '12245', '12284', '11977', '12322']


@bot.message_handler(content_types=['text'])
def login(message):
    set = bot.send_message(message.chat.id, 'Привет, введите логин.')
    bot.register_next_step_handler(set, start)


def start(message):
    if message.text.lower() == 'hmirin':
        bot.delete_message(message.chat.id, message.message_id)
        keyboard = types.InlineKeyboardMarkup()
        serv_iptv = types.InlineKeyboardButton(text='IPTV', callback_data='5.153.136.196')
        serv_calculate = types.InlineKeyboardButton(text='Calculate', callback_data='5.153.136.197')
        keyboard.add(serv_iptv, serv_calculate)
        bot.send_message(message.chat.id, "Приветствую Создатель, вебери сервер.", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Иди в Жопу")


@bot.callback_query_handler(func=lambda call: call.data=='5.153.136.196')
def callback_server(call):
    configurations['serv'] = call.data
    print(configurations)
    keyboard = types.InlineKeyboardMarkup()
    freq_11785 = types.InlineKeyboardButton(text='11785', callback_data='11785')
    freq_11900 = types.InlineKeyboardButton(text='11900', callback_data='11900')
    freq_12245 = types.InlineKeyboardButton(text='12245', callback_data='12245')
    freq_12284 = types.InlineKeyboardButton(text='12284', callback_data='12284')
    keyboard.add(freq_11785, freq_11900)
    keyboard.add(freq_12245, freq_12284)
    bot.send_message(chat_id=call.message.chat.id, text="Выбери частоту", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data=='5.153.136.197')
def callback_server(call):
    configurations['serv'] = call.data
    print(configurations)
    keyboard = types.InlineKeyboardMarkup()
    freq_11977 = types.InlineKeyboardButton(text='11977', callback_data='11977')
    freq_12322 = types.InlineKeyboardButton(text='12322', callback_data='12322')
    keyboard.add(freq_11977, freq_12322)
    bot.send_message(chat_id=call.message.chat.id, text="Выбери частоту", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in freq)
def actions(call):
    configurations['frec'] = call.data
    print(configurations)
    keyboard = types.InlineKeyboardMarkup()
    action_restart = types.InlineKeyboardButton(text="перезагрузить Астру", callback_data='restart')
    actiuon_log = types.InlineKeyboardButton(text="Посмотреть в логе ERROR", callback_data='log')
    keyboard.add(action_restart, actiuon_log)
    bot.send_message(chat_id=call.message.chat.id, text='И что мне с этим делать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data=='log')
def hmirin(call):
    configurations['action'] = call.data
    print(call.data)
    print(configurations)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


print(configurations)
bot.polling()
