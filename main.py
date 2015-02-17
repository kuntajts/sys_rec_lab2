__author__ = 'andrew'
import Spider
from google import search
import os


#

# Get the first 20 hits for "Mariposa botnet" in Google Spain


if not os.path.exists("data/cache"):
    os.makedirs("data/cache")

if not os.path.exists("data/raw"):
    os.makedirs("data/raw")

if not os.path.exists("data/header"):
    os.makedirs("data/header")

if not os.path.exists("data/clean"):
    os.makedirs("data/clean")



books = open("data/item/book.txt", "r")
bookList = []
for book in books:
    bookList.append(book.rstrip())
print(bookList)

movies = open("data/item/movie.txt", "r")
movieList = []
for movie in movies:
    movieList.append(movie.rstrip())
print(movieList)

songs = open("data/item/music.txt", "r")
songList = []
for song in songs:
    songList.append(song.rstrip())
print(songList)
spider = Spider.Spider()
for item in bookList:
    test = 0
    urls = search(item + " book", 'com', 'en', '0', 'off', 0, 0, 10, 2.0, True, {}, '')
    for url in urls:
        print(str(test) +" "+ url)
        test = test + 1
    print("\n\n")

for item in movieList:
    for url in search(item + " movie", 'com', 'en', '0', 'off', 0, 0, 10, 2.0, True, {}, ''):
         if(type(url) is str):
            print(spider.fetch(url, "movie"))

for item in songList:
    for url in search(item + " song", 'com', 'en', '0', 'off', 0, 0, 10, 2.0, True, {}, ''):
         if(type(url) is str):
            print(spider.fetch(url, "song"))

books.close()
movies.close()
songs.close()