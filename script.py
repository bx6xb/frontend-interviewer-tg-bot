import telebot
import random
import os
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import HTML, CSS, JS, TS, REACT, REDUX, NEXT, WEB, GENERAL, QUESTIONS_LIST, CATEGORIES

# get bot token
load_dotenv()

token = os.getenv("TOKEN")

if not token:
    raise ValueError("Токен не найден. Проверьте файл .env и переменную TOKEN.")

bot = telebot.TeleBot(token)

# bot commands

# --- /start ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(HTML),
        KeyboardButton(CSS),
        KeyboardButton(JS),
        KeyboardButton(TS),
        KeyboardButton(REACT),
        KeyboardButton(REDUX),
        KeyboardButton(NEXT),
        KeyboardButton(WEB),
        KeyboardButton(GENERAL),
    )
    bot.send_message(message.chat.id, "Выберите категорию вопросов", reply_markup=markup)


# --- Handler for category questions ---
@bot.message_handler(func=lambda message: message.text in QUESTIONS_LIST)
def handle_random(message):
    category = CATEGORIES[message.text]
    question_id = random.randint(1, category['total'])
    random_question = category[question_id]
    text = f'---Вопрос {question_id}---\n{random_question['question']}\n\n---Ответ---\n{random_question['answer']}'
    bot.send_message(message.chat.id, text)


# bot init
print("Бот запущен и ожидает сообщений...")
bot.polling()
