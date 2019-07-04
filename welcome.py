#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config, handler

# log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    logger.warning('Update "%s" genera errore: "%s"', update, context.error)

# This is the function that initializes the bot
def main():
    updater = Updater(config.bot_token)
    dp = updater.dispatcher
    # Qui richiamo le funzioni senza comando, =>handler
    dp.add_handler(MessageHandler(None, handler.init))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
