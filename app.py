#!/usr/bin/env python

"""REST API"""

from flask import Flask, request
from flask_cors import CORS
import json
import time


app = Flask(__name__)
CORS(app)

users = [
    {'id': 1, 'user': 'Kacper', 'password': 'password'}
]

shopping_list = [
    {'id': 1, 'name': 'milk', 'quantity': 2, 'date': '2022-05-04', 'owner': 'Kacper'},
    {'id': 2, 'name': 'water', 'quantity': 3, 'date': '2022-05-04', 'owner': 'Kacper'},
    {'id': 3, 'name': 'bread', 'quantity': 1, 'date': '2022-05-04', 'owner': 'Kacper'}
]

categories = [
    {'id': 1, 'name': 'Drink'},
    {'id': 2, 'name': 'Candy'}
]

products = [
    {'id': 1, 'name': 'Chocolate', 'category_id': 2},
    {'id': 2, 'name': 'Water', 'category_id': 1}
]

history = [
    {'id': 1, 'quantity': 3, 'price': 4.50, 'date': '2022-05-01', 'owner': 'Kacper', 'product_id': 2},
    {'id': 2, 'quantity': 4, 'price': 3.13, 'date': '2022-05-03', 'owner': 'Kacper', 'product_id': 1},
]

################ User ################
@app.route('/login', methods=['POST'])
def login():
    pass


################ Shopping List ################
@app.route('/getShoppingList')
def getShopppingList():
    return {'data': shopping_list}


@app.route('/addShoppingListElement', methods=['POST'])
def addShoppingListElement():
    id = shopping_list[-1]['id'] + 1
    data = json.loads(request.data)
    data['id'] = id
    shopping_list.append(data)
    return {'data': id}


@app.route('/delShoppingListElement', methods=['DELETE'])
def delShoppingListElement():
    id = json.loads(request.data)
    for i in range(len(shopping_list)):
        if shopping_list[i]['id'] == int(id):
            del shopping_list[i]
            return {'status': 'ok'}
    return 'Record not found', 400


################ Categories ################
@app.route('/getCategories')
def getCategories():
    return {'data': categories}


@app.route('/addCategory', methods=['POST'])
def addCategory():
    id = categories[-1]['id'] + 1
    data = json.loads(request.data)
    data['id'] = id
    categories.append(data)
    return {'data': id}


@app.route('/getCategoryNames')
def addCategoryNames():
    new_data = []
    for element in categories:
        new_data.append({
            'id': element['id'],
            'name': element['name']
        })
    return {'data': new_data}


@app.route('/editCategory', methods=['POST'])
def editCategory():
    data = json.loads(request.data)
    for i in range(len(categories)):
        if categories[i]['id'] == int(data['id']):
            categories[i] = {'id': data['id'], 'name': data['name']}
            return {'status': 'ok'}
    return 'Record not found', 400


################ Products ################
@app.route('/getProducts')
def getProducts():
    return {'data': products}


@app.route('/getProductNames')
def getProductNames():
    new_data = []
    for element in products:
        new_data.append({
            'id': element['id'],
            'name': element['name']
        })
    return {'data': new_data}


@app.route('/addProduct', methods=['POST'])
def addProduct():
    id = products[-1]['id'] + 1
    data = json.loads(request.data)
    data['id'] = id
    products.append(data)
    return {'data': id}


@app.route('/editProduct', methods=['POST'])
def editProduct():
    data = json.loads(request.data)
    for i in range(len(products)):
        if products[i]['id'] == int(data['id']):
            products[i] = {'id': data['id'], 'name': data['name'], 'category_id': data['category_id']}
            return {'status': 'ok'}
    return 'Record not found', 400


################ History ################
@app.route('/getHistory')
def getHistory():
    return {'data': history}


@app.route('/addHistory', methods=['POST'])
def addHistory():
    id = history[-1]['id'] + 1
    data = json.loads(request.data)
    data['id'] = id
    history.append(data)
    return {'data': id}


@app.route('/editHistory', methods=['POST'])
def editHistory():
    data = json.loads(request.data)
    for i in range(len(history)):
        if history[i]['id'] == int(data['id']):
            history[i] = {'id': data['id'], 'quantity': data['quantity'], 'price': data['price'], 'date': data['date'], 'owner': data['owner'], 'product_id': data['product_id']}
            return {'status': 'ok'}
    return 'Record not found', 400


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
