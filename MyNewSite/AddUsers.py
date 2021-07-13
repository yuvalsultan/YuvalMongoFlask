
import json
from exten import mongo
from website import create_app

#the func 'create_users' reads data from json file and loads it to DB
#This file runs just one time
app = create_app()
app.app_context().push()


def create_users():

    my_users = mongo.db.Users

    f = open('MyUsers.json')
    data = json.load(f)
    for i in data:
        first_name = i['first_name']
        email = i['email']
        password = i['password']
        user = my_users.find_one({"email": email})
        if user:
            return 'already in DB'
        else:
            my_users.insert_one({'email': email, 'first_name': first_name, 'password': password})
        
    print('Good Sign')


create_users()
