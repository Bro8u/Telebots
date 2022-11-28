import pymongo
import telebot
import config

 
bot = telebot.TeleBot(config.token)
client = pymongo.MongoClient("mongodb+srv://Boris:work12345@cluster0.f4niuck.mongodb.net/?retryWrites=true&w=majority")
db = client.testdata
coll = db.users
@bot.message_handler(content_types=["text"])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать')
	us_id = message.from_user.id
	us_name = message.from_user.first_name
	us_sname = message.from_user.last_name
	username = message.from_user.username
	if(coll.find_one({"id": us_id}) == None):
		coll.insert_one({"id" : us_id, "user_name" : us_name, "user_surname" : us_sname, "username" : username})
 

if __name__ == '__main__':
     bot.infinity_polling()
