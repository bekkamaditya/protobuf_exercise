import sys
import movie_pb2

def updateMovie(fileName) :
    movie_list = movie_pb2.Movie_list();
    try:
      with open(fileName, "rb") as f:
        movie_list.ParseFromString(f.read())
    except IOError:
      print fileName + ": File not found.  Creating a new file."
    while True:
        name = raw_input("Movie name to be updated(or leave blank to finish): ")
        if name == "" :
            break ;
        flag = True
        index = -1 ;
        for movie in movie_list.movies :
            index = 0;
            if movie.name == name:
                field = raw_input("Enter field to be updated: ")
                flag = False
                break
        if flag:
            print "Movie not found.Continuing...."
