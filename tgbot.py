import sys
import telebot
from telebot import types 

import sqlite3 
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import Column, Integer, String

#DATABASE_NAME = 'products_in_stock.sqlite'

#engine = create_engine(f'sqlite:///{DATABASE_NAME}')
#Session = sessionmaker(bind=engine)

Base= declarative_base()


# def create_db():
#   # Base.metadata.create_all(engine)

class Products(Base):
    __tablename__ = 'our_products_in_stock'

    number = Column(Integer, primary_key = True) #номер товара по счету
    unit = Column(String)    #наименование товара
    vendor_code = Column(Integer)   #артикул
    amount = Column(Integer)        #количество позиций на складе
    price = Column(Integer) #цена товара


engine = create_engine(f'sqlite:///our_products_in_stock.db')


Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# productOne = Products(unit = "Футболка белая", vendor_code = 1843, amount = 46,  price = 1990 )
# productTwo = Products(unit = "Брюки черные", vendor_code = 7602, amount = 25,  price = 3499 )
# productThree = Products(unit = "Пальто в клетку", vendor_code = 6179, amount = 12,  price = 7990 )
# productFour = Products(unit = "Ботинки на шнуровке", vendor_code = 4305, amount = 51,  price = 5199 )

# session.add(productOne)
# session.add(productTwo)
# session.add(productThree)
# session.add(productFour)
# session.commit()



bot = telebot.TeleBot('5738649645:AAHDFa9pAp0IPbXG_Bdd9ryLCQLFniLDK0s')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Доброго времени суток!</b>', parse_mode = 'html')


@bot.message_handler(commands=['work'])
def work(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Посмотреть товар на складе: /base')
    btn2 = types.KeyboardButton('Добавить товар в базу: /editbase')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)



bot.polling(none_stop=True)


