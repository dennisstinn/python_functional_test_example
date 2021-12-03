from flask import Flask, request, jsonify
import uuid
from base64 import urlsafe_b64encode

app = Flask(__name__)

# TODO: remove seeding car
master_cars = {"cars": [{"key": "7B7B2797DF6F4075", "model": "Ford F510", "year": "2017", "miles": 213789}]}


@app.route('/', methods=['GET'])
def read_records():
    # return all of the records
    return jsonify(master_cars)

@app.route('/', methods=['POST'])
def create_record():
    # TODO: wrap marshalling in try/catch
    payload = request.get_json(force=True)

    car = {}
    if 'model' in payload:
        car["model"] = payload['model']
    else:
        return ('Error model not found', 403)
    
    if 'year' in payload:
        car['year'] = payload['year']
    else:
        return 'Error year not found', 403

    if 'miles' in payload:
        car['miles'] = payload['miles']
    else:
        return 'Error miles not found', 403

    car['key'] = uuid.uuid4().hex[:16].upper()

    master_cars['cars'].append(car)
    return jsonify(car) 

    
@app.route('/<delete_key>', methods=['DELETE'])
def delete_record(delete_key):
    # loop though all of the cars, delete key if found

    for car in master_cars['cars']:
        if 'key' in car:
            if car['key'] == delete_key:
                master_cars['cars'].remove(car)
                return '', 204

    return f'not found: {delete_key}', 404


app.run(host='127.0.0.1', port=8080, debug=True)
