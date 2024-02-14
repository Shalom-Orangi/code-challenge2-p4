from flask import Flask,make_response,jsonify,request
from flask_migrate import Migrate
from models import Restaurant,Pizza,RestaurantPizza,db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

migrate=Migrate(app,db)

db.init_app(app)

@app.route('/restaurants',methods=['GET'])
def get_restaurants():
    restaurants=Restaurant.query.all()
    restaurants_data=[
        {"id":restaurant.id,
         "name":restaurant.name,
         "address":restaurant.address}
        for restaurant in restaurants
    ]
    
    response=make_response(
        jsonify(restaurants_data),
        200
    )
    return response

@app.route('/restaurant/:id',methods=['GET','DELETE'])
def get_restaurants_by_id(id):
    restaurant=Restaurant.query.filter_by(id==id).first()

    if request.method=='GET':
        restaurant_dict=restaurant.to_dict()

        response=make_response(
            jsonify(restaurant_dict),
            200
        )
        return response
    
    if restaurant is None:
        response=make_response({"error":"Restaurant not found"})
    
    if request.method =='DELETE':
        db.session.delete(restaurant)
        db.session.commit()

        response_body={}

        response=make_response(
            jsonify(response_body),
            200
        )
        return response

    if restaurant is None:
        response=make_response({"error":"Restaurant not found"})


@app.route('/pizzas',methods=['GET'])
def get_pizzas():
    pizzas=Pizza.query.all()
    pizzas_data=[
        {"id":pizza.id,"name":pizza.name,"ingredients":pizza.ingredients}
        for pizza in pizzas
    ]

    response=make_response(
        jsonify(pizzas_data),
        200
    )
    return response

@app.route('/restaurant_pizzas',methods=['POST'])
def get_restaurants_pizzas():
    if request.method =='POST':
        new_restaurant_pizza=RestaurantPizza(
            price=request.form.get('price'),
            pizza_id=request.form.get('pizza_id'),
            restaurant_id=request.form.get('restaurant_id'),
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        restaurant_pizza_dict=new_restaurant_pizza.to_dict()

        response=make_response(
            jsonify(restaurant_pizza_dict),
            200
        )
        return response

if __name__=="__main__":
    app.run(port=5555)