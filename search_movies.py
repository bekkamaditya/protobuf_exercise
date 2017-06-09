import movie_pb2
import sys
import pickle
import bsddb3
from list_movies import listMovie

def searchByGenre(db):
    temp = raw_input("Enter genre you wish to search by(adventure/sci_fi/drama): ")
    if temp.upper() == "ADVENTURE" :
        genre = movie_pb2.ADVENTURE
    elif temp.upper() == "SCI_FI" :
        genre = movie_pb2.SCI_FI
    elif temp.upper() == "DRAMA" :
        genre = movie_pb2.DRAMA
    flag = True
    for key in db.keys() :
    	movie = pickle.loads( db[key] )
        for g in movie.genres :
            if g == genre :
                listMovie(movie)
                flag = False
                break
    if flag:
        print "No results found\n"

def searchByActor(db):
    temp = raw_input("Actor name: ")
    temp = temp.upper()
    flag = True
    for key in db.keys() :
    	movie = pickle.loads( db[key] )
        for actor in movie.actors :
            if actor.upper() == temp :
                listMovie(movie)
                flag = False
                break
    if flag:
        print "No results found\n"

def searchByDir(db):
    temp = raw_input("Director name: ")
    temp = temp.upper()
    flag = True
    for key in db.keys() :
    	movie = pickle.loads( db[key] )
        for director in movie.directors :
            if director.upper() == temp :
                listMovie(movie)
                flag = False
                break
    if flag:
        print "No results found\n"

def searchMovies():
    db = bsddb3.hashopen('movies.db','r') 
    while True:
        category = raw_input("Search by(genre/actor/director): ")
        if category.upper() == "GENRE" :
            searchByGenre(db)
        elif category.upper() == "ACTOR" :
            searchByActor(db)
        elif category.upper() == "DIRECTOR" :
            searchByDir(db)
        if raw_input("Do you want to search more(or leave blank to finish): ") == "" :
            break
