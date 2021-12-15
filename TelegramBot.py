from telegram import Update
import configparser
from telegram.ext import Updater, CommandHandler

import numpy
import pandas

from collections import Counter

HELLO_MS = 'سلام! کلمه‌ای که می‌خوای رو بنویس، تا توی فایل اکسلی که داده بودین ببنیم چه کسایی و هرکدوم چند بار، ازش استفاده کردن.'

def start_handler(update, context):
    



def main():

    config = configparser.ConfigParser()
    config.read('token.ini')
    token = config['telegram']['MyPytBot']

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))



    df = pd.read_excel('Requests.xlsx')





    target_df = df[df['توضیحات'].str.contains('واتساپ')]
    target_df = target_df['نام درخواست کننده']
    target_df = np.asanyarray(target_df)
    res = Counter(target_df)



if __name__ == '__main__':
    main()
