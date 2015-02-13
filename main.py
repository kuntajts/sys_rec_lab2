__author__ = 'andrew'
import Spider
from google import search


#

# Get the first 20 hits for "Mariposa botnet" in Google Spain

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
    for url in search(item + " book"):
        if(type(url) is str):
            print(spider.fetch(url, "book"))

for item in movieList:
    for url in search(item + " movie"):
         if(type(url) is str):
            print(spider.fetch(url, "movie"))

for item in songList:
    for url in search(item + " song"):
         if(type(url) is str):
            print(spider.fetch(url, "song"))

books.close()
movies.close()
songs.close()