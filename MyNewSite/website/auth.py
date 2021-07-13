from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from exten import mongo
from website.models import movie_wish_list


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        my_users = mongo.db.Users

        email = request.form.get('email')
        password = request.form.get('password')

        user = my_users.find_one({'email': email})

        if user:
            if password == user['password']:
                flash('Logged in successfully!', category='success')
                session['email'] = email
                movies = user['movie']
                for i in movies:
                    movie_wish_list.append(i)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")


@auth.route('/logout')
def logout():
    session.pop('email', None)
    movie_wish_list.clear()
    return redirect(url_for("auth.login"))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        my_users = mongo.db.Users
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = my_users.find_one({"email": email})

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            my_users.insert_one({'email': email, 'first_name': first_name, 'password': password1})
            flash('Account created!', category='success')
            session["email"] = email
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
