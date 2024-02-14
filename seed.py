from random import randint, choice
from faker import Faker
from app import app
from models import db, Restaurant, Pizza,RestaurantPizza

fake = Faker()

with app.app_context():

    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    # Seed pizza
    ingredients_data= [
        {"name":"Veggie Pizza",
         "ingredients": "Dough,TomatoSauce,Cheese,Veggies",
        },
        {"name":"Pepperoni",
         "ingredients": "Dough,TomatoSauce,Cheese,Pepperoni"
        },
        {"name":"Chicken BBQ",
         "ingredients": "Dough,TomatoSauce,Cheese,Chicken,BBQ Sauce"},
        {"name":"Meat Deluxe",
         "ingredients": "Dough,TomatoSauce,Cheese,Tomatoes,Beef"}
    ]

    pizzas = []
    for pizza_info in ingredients_data:
        pizza = Pizza(**pizza_info)
        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()

    # Seed restaurants
    restaurants_data = [
        {"name": "Pizza Inn"},
        {"name": "Dominos"},
        {"name": "Pizza Hut"},
        {"name": "Pizza Haven"},
        {"name": "Mambo Italia"},
        {"name": "Romans pizza"},
        {"name": "Pizza Connection"},
        {"name": "Steers"},
        {"name": "Pizzeria" },
        
    ]

    restaurants = []
    for restaurant_info in restaurants_data:
        restaurant= Restaurant(
            **restaurant_info,
            address=fake.street_address(),
            pizza_id=pizza.id,
            )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()

    # Seed restaurantpizzas
    pizza=Pizza.query.all()
    restaurants=Restaurant.query.all()

    for pizza in pizzas:
        for restaurant in restaurants:
            price= randint(0,30)

            restaurant_pizza=RestaurantPizza(
                price=price,
                pizza_id=pizza.id,
                restaurant_id=restaurant.id,

            )
            db.session.add(restaurant_pizza)

    db.session.commit()