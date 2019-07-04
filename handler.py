import random
import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

#WELCOME
def welcome(bot, update):
	for new in update.message.new_chat_members:
		update.message.reply_text('Welcome here {username} in {chat_title}'
			.format(username=update.message.from_user.first_name, chat_title=update.message.chat.title))
		
#declaration functions
def init(bot, update):
	welcome(bot, update)
	
	


