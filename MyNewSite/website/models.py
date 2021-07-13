import requests


class Movie:
    name = ''
    img = ''
    summary = ''
    genre = ''
    link = ''
    rate = ''

    def __init__(self, name, img, summary, genre, link, rate):
        self.name = name
        self.img = img
        self.summary = summary
        self.genre = genre
        self.link = link
        self.rate = rate


r = requests.get('https://itunes.apple.com/us/rss/topmovies/limit=25/json')
info = r.json()
movies = info['feed']['entry']
movie_list = []
movie_wish_list = []
for s in movies:
    name = s['im:name']['label']
    img = s['im:image'][2]['label']
    summary = s['summary']['label']
    genre = s['category']['attributes']['term']
    link = s['link'][0]['attributes']['href']
    new_movie = Movie(name=name, img=img, summary=summary, genre=genre, link=link, rate='')
    movie_list.append(new_movie)
