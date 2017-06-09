import sys
import movie_pb2
from search_movies import *
from list_movies import *
from add_movie import *
from delete import *

while True :
    print "Choose your action"
    action = raw_input("add/Search/Delete/Update/ShowAll(or leave blank to finish): ")
    if action == "" :
        break
    if action.lower() == "add" :
        addMovie()
    if action.lower() == "search" :
        searchMovies()
    elif action.lower() == "delete" :
        deleteMovie()
    elif action.lower() == "update" :
        updateMovie()
    elif action.lower() == "showall" :
        ListAllMovies()
