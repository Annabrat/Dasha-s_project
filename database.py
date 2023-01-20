import sqlite3 as lite
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import Column, Integer, String


Base= declarative_base()

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

# con = lite.connect('our_products_in_stock.db')
# with con:
#     cur = con.cursor()
#     cur.execute ("SELECT * FROM Products")
#     rows = cur.fetchall()

#     for row in rows:
#         print (row)
