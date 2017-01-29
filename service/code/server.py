import ConfigParser
import json
import logging
import os

# 3rd party libs
import bottle
from mongoengine import *

import constants

config_path = '../config/conf'
password_encode = 'base64'
app = bottle.Bottle()
config = ConfigParser.RawConfigParser()
config.read(os.path.abspath(__file__+'../../../config/conf'))
connect(config.get('mongo', 'Database'), config.get('mongo', 'IP'))


class User(Document):
    _id = StringField(unique=True)
    email = StringField(required=True, unique=True)
    username = StringField()
    password = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    phone = StringField(required=True)
    location = ListField(StringField)
    favorites = ListField(StringField)
    dislikes = ListField(StringField)
    meta = {'collection': 'user'}


def _success_response(response):
    response.status = 200
    response.content_type = 'application/json'


def _login_success_json_data(user_id, email, location = [], favourites = [], dislikes=[]):
    return json.dumps({
        'data': {
            'id': user_id,
            'email': email,
            'location': location,
            'favourites': favourites,
            'dislikes': dislikes
        }
    })


@app.route('/users', method='post')
def create_user():
    data = bottle.request.json
    try:
        event = User(
            email=data[constants.email],
            username=data['username'],
            password=data['password'].encode(password_encode),
            first_name=data['firstname'],
            last_name=data['lastname'],
            phone=data['phone'],
            favorites=[],
            dislikes=[]
        ).save()
        _success_response(bottle.response)
        return _login_success_json_data(event.id, data[constants.email])
    except Exception as e:
        logging.error(e)
        bottle.response.status = 400
        return json.dumps(
            {
                'error_details': e
            })


@app.route('/users/forget_password', method='get')
def forget_password():
    data = bottle.request.json
    try:
        user = User.objects.get(email=data[constants.email])
        if user is None:
            raise Exception('User does not exist')
        else:
            _success_response(bottle.response)
    except Exception as e:
        logging.error(e)
        bottle.response.status = 400
        return json.dumps({
            'error_details': e
        })


@app.route('/login', method='post')
def login():
    data = bottle.request.json
    try:
        user = User.objects.get(email=data[constants.email])
        if user is None:
            raise Exception('User doesn\'t exist')
        if user.password == data['password'].encode(password_encode):
            _success_response(bottle.response)
            return _login_success_json_data(user.id, user.email, user.location, user.favorites, user.dislikes)
        else:
            raise Exception('Wrong password')
    except Exception as e:
        logging.error(e)
        bottle.response.status = 500
        return json.dumps({
            'error_details': e
        })


@app.route('/user/operation')


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format=('%(asctime)s [%(process)d] [%(levelname)s] '
                '[%(module)s.%(funcName)s:%(lineno)d]: %(message)s'),
        datefmt='%Y-%m-%d %H:%M:%S'
    )


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=8000)
