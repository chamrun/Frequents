from telegram import Update, ParseMode
import configparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import numpy as np
import pandas as pd

from collections import Counter

HELLO_MS = 'سلام! کلمه‌ای که می‌خوای رو بنویسین، تا توی فایل اکسلی که داده بودین ببنیم چه کسایی و هرکدوم چند بار، ازش ' \
           'استفاده کردن. '
NOT_FOUND_MS = 'چیزی پیدا نکردیم.'

df = pd.read_excel('Requests.xls')


def start_handler(update: Update, context):
    update.message.reply_text(text=HELLO_MS)
    user = update.effective_user
    context.bot.send_message(chat_id='184585885',
                             text=fr'{user.mention_markdown_v2()}',
                             parse_mode=ParseMode.MARKDOWN_V2)


def searcher(update: Update, context):
    key = update.message.text
    target_df = df[df['توضیحات'].str.contains(key)]
    target_df = target_df['نام درخواست کننده']
    target_df = np.asanyarray(target_df)
    counter = Counter(target_df)

    result = ''
    for line in counter:
        result += str(line) + ': ' + str(counter[line]) + '\n'

    if result == '':
        result = NOT_FOUND_MS

    update.message.reply_text(text=result)


def main():

    config = configparser.ConfigParser()
    config.read('token.ini')
    token = config['telegram']['MyPytBot']

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, searcher))
    print('Trying to start...')
    updater.start_polling()
    print("Started.")
    updater.idle()
    print("End!")


if __name__ == '__main__':
    main()
