__author__ = 'andrew'
import Spider
from google import search
import random


#

# Get the first 20 hits for "Mariposa botnet" in Google Spain


books = open("data/item/book.txt", "r")
bookList = []
for book in books:
    bookList.append(book.rstrip())

movies = open("data/item/movie.txt", "r")
movieList = []
for movie in movies:
    movieList.append(movie.rstrip())

songs = open("data/item/music.txt", "r")
songList = []
for song in songs:
    songList.append(song.rstrip())

spider = Spider.Spider()
for item in bookList:
    urls = search(item + " book", 'com', 'en', '0', 'off', 1, 0, 11, random.uniform(10.0, 60.0), True, {}, '')
    for url in urls:
         if(type(url) is str):
            print(spider.fetch(url, "movie"))

for item in movieList:
    for url in search(item + " movie", 'com', 'en', '0', 'off', 1, 0, 11, random.uniform(10.0, 60.0), True, {}, ''):
         if(type(url) is str):
            print(spider.fetch(url, "movie"))

for item in songList:
    for url in search(item + " song", 'com', 'en', '0', 'off', 1, 0, 11, random.uniform(10.0, 60.0), True, {}, ''):
         if(type(url) is str):
            print(spider.fetch(url, "song"))

books.close()
movies.close()
songs.close()