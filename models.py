from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db=SQLAlchemy()

class Restaurant(db.Model):
    __tablename__='restaurants'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    address=db.Column(db.String)
    pizza_id=db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    #rel
    pizza=db.relationship('Pizza',back_populates='restaurant')
    restaurantpizza=db.relationship('RestaurantPizza',back_populates='restaurant')


    def __repr__(self) :
        return f'<{self.id},{self.name},{self.address}>'
    
class Pizza(db.Model):
    __tablename__='pizzas'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)

    #rel
    restaurant=db.relationship('Restaurant',back_populates='pizza')
    restaurantpizza=db.relationship('RestaurantPizza',back_populates='pizza')

    def __repr__(self) :
        return f'<{self.id},{self.name},{self.ingredients}>'
    
class RestaurantPizza(db.Model):
    __tablename__='restaurantpizzas'

    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer)
    pizza_id=db.Column(db.Integer,db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurants.id"))

    #rel
    pizza=db.relationship('Pizza',back_populates='restaurantpizza')
    restaurant=db.relationship('Restaurant',back_populates='restaurantpizza')

    #validations
    @validates('price')
    def validate_price(self,key,price):
        if len(price)<1 or len(price)>30:
            raise ValueError("price must be between 1-30")
        return price

    def __repr__(self) :
        return f'<{self.price},{self.pizza_id},{self.restaurant_id},>'