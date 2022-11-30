import pymongo
import telebot
import config
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
client = pymongo.MongoClient("mongodb+srv://Boris:work12345@cluster0.f4niuck.mongodb.net/?retryWrites=true&w=majority")
db = client.testdata
coll = db.cafes
@bot.message_handler(content_types=["text"])
def start_message(message):	
	f = message.text
	f = f.lower()
	a = ""
	for value in coll.find({"adress": f}):
		b = ""
		for v in value:
			if (v != "_id"):
				b += (v + " - " + value[v] + ", ")
		a += b[:-2] + "\n"
	bot.send_message(message.chat.id, a)
if __name__ == '__main__':
     bot.infinity_polling()
