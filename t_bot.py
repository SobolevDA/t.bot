import telebot
from parse_site import parse, base_url, headers


bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == 'start':
        info = parse(base_url, headers)
        for value in info.values():
            #bot.send_message(message.chat.id, key)
            bot.send_message(message.chat.id, value)
        #print(info.values())
            #print(key, " => ", value)


bot.polling()
