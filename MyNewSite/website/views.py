from flask import Blueprint, render_template, session, redirect,url_for,flash, request
from website.models import movie_list, movie_wish_list
views = Blueprint('views', __name__)
from exten import mongo


@views.route('/', methods=['GET', 'POST'])
def home():
    if 'email' in session:
        if request.method == 'POST':
            movie_name = request.form['MovieName']
            my_users = mongo.db.Users
            if movie_name in movie_wish_list:
                flash('Movie is already in wish list')
            else:
                movie_wish_list.append(movie_name)
                my_users.find_one_and_update({'email': session['email']}, {"$set": {'movie': movie_wish_list}})

        return render_template("home.html", movie_list=movie_list)
    else:
        flash('Log in first', category='success')
        return redirect(url_for("auth.login"))

@views.route('/wishList')
def wishlist():
    if 'email' in session:
        for_real_wish = []
        my_users = mongo.db.Users
        user = my_users.find_one({'email': session['email']})
        user_movies = user['movie']
        for i in user_movies:
            for movie in movie_list:
                if i == movie.name:
                    for_real_wish.append(movie)
        return render_template("WishList.html", ForRealWish=for_real_wish)
    else:
        flash('Log in first', category='success')
        return redirect(url_for("auth.login"))





