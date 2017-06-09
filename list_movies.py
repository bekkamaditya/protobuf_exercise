import movie_pb2
import sys
import pickle
import bsddb3

def ListAllMovies():
    db = bsddb3.hashopen('movies.db','r')
    flag = True
    for key in db.keys() :
        flag = False
        listMovie( pickle.loads(db[key]) )
    if flag:
        print "No movies found"

def listMovie(movie) :
    print "Movie name: " + movie.name
    temp = "Directors: " ;
    for director in movie.directors :
        temp += director + ", "
    print temp
    temp = "Actors: " ;
    for actor in movie.actors :
        temp += actor + ", "
    print temp
    temp = "Genres: " ;
    for genre in movie.genres :
        if genre == movie_pb2.ADVENTURE :
            temp += "Adventure, "
        elif genre == movie_pb2.SCI_FI :
            temp += "Sci_fi, "
        elif genre == movie_pb2.DRAMA :
            temp += "Drama, "
    print temp
    temp = "Languages: " ;
    for language in movie.languages :
        temp += language + ", "
    print temp
    print "Run time: " + str(movie.runTime)
    if movie.productionHouse != "" :
        print "Production House: " + movie.productionHouse
    if movie.country != "" :
        print "Country: " + movie.country
    temp = "Release Date: " + str(movie.releaseDate.day) + "/"
    mon = movie.releaseDate.month ;
    if mon == movie_pb2.JANUARY:
        temp += "01"
    elif mon == movie_pb2.FEBRUARY:
        temp += "02"
    elif mon == movie_pb2.MARCH:
        temp += "03"
    elif mon == movie_pb2.APRIL:
        temp += "04"
    elif mon == movie_pb2.MAY:
        temp += "05"
    elif mon == movie_pb2.JUNE:
        temp += "06"
    elif mon == movie_pb2.JULY:
        temp += "07"
    elif mon == movie_pb2.AUGUST:
        temp += "08"
    elif mon == movie_pb2.SEPTEMBER:
        temp += "09"
    elif mon == movie_pb2.OCTOBER:
        temp += "10"
    elif mon == movie_pb2.NOVEMBER:
        temp += "11"
    elif mon == movie_pb2.DECEMBER:
        temp += "12"
    temp += "/" + str(movie.releaseDate.year)
    print temp

    print "Reviews: "
    flag = True
    for review in movie.reviews :
        flag = False
        print "User: " + review.userName
        print "Rating: " +str(review.rating)
        print "Comment: " + review.comment + "\n"
    if flag:
        print "None to show\n"
