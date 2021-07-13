from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from pymongo import  MongoClient
import bcrypt

from website import create_app
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)