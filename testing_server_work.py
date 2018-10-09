import requests as re
import time

tg_token = "674053533:AAHrvZqdHz-5EdbsjKPg86UjEPzhl7sdnKc"
url_tg = "https://api.telegram.org/bot674053533:AAHrvZqdHz-5EdbsjKPg86UjEPzhl7sdnKc/{}"


def send_message(chat_id, text, flag=False, keyboard=False):
    if not keyboard:
        message = re.get(url_tg.format("sendMessage"), params={'chat_id': chat_id, 'text': text,
                                                               'disable_web_page_preview': flag, 'parse_mode': 'HTML'})
    else:
        message = re.get(url_tg.format("sendMessage"), params={'chat_id': chat_id, 'text': text,
                                                               'reply_markup': keyboard})
    return message

while True:
    send_message(165954182, "Я работаю!")
    time.sleep(30)
