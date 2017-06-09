import bsddb3
import pickle
import movie_pb2 

db = bsddb3.hashopen('movies.db','c')
for key in db.keys():
    #print key 
    movie = movie_pb2.Movie();
    movie = pickle.loads(db[key])
    print movie.name
    temp = ""
    for actor in movie.actors:
	temp += actor + ","
    print "Actors: " + temp
    
    temp = ""
    for director in movie.directors:
	temp += director + ","
    print "Directors: " + temp
    
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
