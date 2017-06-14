import sys
import movie_pb2
import pickle
import bsddb3

def deleteMovie() :
    # file storage to database storage
    db = bsddb3.hashopen('movies.db','c')
    
    while True:
        name = raw_input("Movie name to be deleted: ")
        flag = True
        index = -1
        for key in db.keys():
	    index = index + 1
            if (pickle.loads(db[key])).name == name :
                del db[key]
	        flag = False
	# File storage to database storage
        if flag:
            print "Movie not found.Continuing...."
        if raw_input("Do you want to delete another movie(or leave blank to finish): ") == "" :
            break
