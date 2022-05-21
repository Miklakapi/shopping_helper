
history = [
    {'id': 1, 'quantity': 3, 'price': 4.50, 'date': '2022-05-01', 'owner': 'Kacper', 'product_id': 2},
    {'id': 2, 'quantity': 4, 'price': 3.13, 'date': '2022-05-03', 'owner': 'Kacper', 'product_id': 1},
]
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
