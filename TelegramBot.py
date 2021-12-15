from telegram import Update
import configparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import numpy as np
import pandas as pd

from collections import Counter

HELLO_MS = 'سلام! کلمه‌ای که می‌خوای رو بنویس، تا توی فایل اکسلی که داده بودین ببنیم چه کسایی و هرکدوم چند بار، ازش ' \
           'استفاده کردن. '

df = pd.read_excel('Requests.xlsx')


def start_handler(update: Update, context):
    update.message.reply_text(text=HELLO_MS)


def searcher(update: Update, context):
    key = update.message.text
    target_df = df[df['توضیحات'].str.contains(key)]
    target_df = target_df['نام درخواست کننده']
    target_df = np.asanyarray(target_df)
    counter = Counter(target_df)

    result = ''
    for line in counter:
        result = str(line) + ': ' + str(counter[line]) + '\n'

    update.message.reply_text(text=result)


def main():

    config = configparser.ConfigParser()
    config.read('token.ini')
    token = config['telegram']['MyPytBot']

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, searcher))

    updater.start_polling()
    print("Started.")
    updater.idle()
    print("End!")


if __name__ == '__main__':
    main()
