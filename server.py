import sys
import movie_pb2
import grpc 
import movie_pb2_grpc
import time
import bsddb3
from concurrent import futures
import pickle
#from add_movie import * 

def createResponse(result):
    temp = movie_pb2.Movie()
    temp.name = result
    responses = movie_pb2.Response()
    responses.movie = temp     
    return responses

def searchByGenre(db,temp):
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
                #listMovie(movie)
                flag = False
		yield movie
                break
    if flag:
        yield createResponse("NO_RESULTS_FOUND")
	return

def searchByDirector(db,temp):
    temp = temp.upper()
    flag = True
    for key in db.keys() :
        movie = pickle.loads( db[key] )
        for director in movie.directors :
            if director.upper() == temp :
                #listMovie(movie)
		yield movie
                flag = False
                break
    if flag:
        yield createResponse("NO_RESULTS_FOUND")
   	return

def searchByActor(db,temp):
    temp = temp.upper()
    flag = True
    for key in db.keys() :
        movie = pickle.loads( db[key] )
        for actor in movie.actors :
            if actor.upper() == temp :
                #listMovie(movie)
		yield movie
                flag = False
                break
    if flag:
        yield createResponse("NO_RESULTS_FOUND")
   	return
     
def addMovieService(arg):
    movie = pickle.loads(arg)
    #addToDB(movie)
    db = bsddb3.hashopen('movies.db','c')
    db[pickle.dumps(movie.name)] = pickle.dumps(movie) 
    yield createResponse("SUCCESS")
    return

def searchMovieService(arg):
    request = pickle.loads(arg)
    db = bsddb3.hashopen('movies.db','c')
    if request.searchBy == movie_pb2.ACTOR:
	responses = searchByActor(db,request.word)
    elif request.searchBy == movie_pb2.DIRECTOR:
	responses = searchByDirector(db,request.word)
    elif request.searchBy == movie_pb2.GENRE:
	responses = searchByGenre(db,request.word)
    return responses

def updateMovieService(arg):
    request = pickle.loads(arg)
    movie = pickle.loads( db[pickle.dumps(request.movieName)] )
    if request.category == movie_pb2.ACTOR :
	del movie.actors[:]
  	for actor in (pickle.loads(request.value)).split(','):
	    movie.actors.append(actor)
    elif request.category == movie_pb2.DIRECTOR :
	del movie.directors[:]
  	for director in (pickle.loads(request.value)).split(','):
	    movie.directors.append(director)
    elif request.category == movie_pb2.GENRE :
	del movie.genres[:]
	for genre in (pickle.loads(request.value)).split(','):
	    if genre.upper() == 'ADVENTURE' :
		movie.genres.append( movie_pb2.ADVENTURE )
	    elif genre.upper() == 'SCI_FI' :
		movie.genres.append( movie_pb2.SCI_FI )
	    elif genre.upper() == 'DRAMA' :
		movie.genres.append( movie_pb2.DRAMA )
    elif request.category == movie_pb2.NAME :
	movie.name = pickle.loads(request.value)
    elif request.category == movie_pb2.RUN_TIME :
	movie.runTime = pickle.loads(request.value)
    elif request.category == movie_pb2.PRODUCTION_HOUSE :
	movie.productionHouse = pickle.loads(request.value)
    elif request.category == movie_pb2.COUNTRY :
	movie.country = pickle.loads(request.value)
    elif request.category == movie_pb2.RELEASE_DATE :
	#will update later
	del movie.languages[:] 
    elif request.category == movie_pb2.LANGUAGES :
	del movie.languages[:]
  	for language in (pickle.loads(request.value)).split(','):
	    movie.languages.append(language)

def showMovieService(arg):
    db = bsddb3.hashopen('movies.db','c')
    index = -1     
    for key in db.keys():
	index = index + 1
	yield pickle.loads(db[key])
    if index == -1:
	yield createResponse("NONE_TO_SHOW") 
	return
    yield createResponse("SUCCESS")
    return

def deleteMovieService(arg):
    db = bsddb3.hashopen('movies.db','c')
    index = -1     
    flag = True
    for key in db.keys():
	index = index + 1
	if (pickle.loads(db[key])).name == arg :
	    del db[key]
	    flag = False
 	    break
    if flag:
	yield createResponse("NOT_FOUND")
	return
    if index == -1:
	yield createResponse("NONE_TO_DELETE") 
	return
    yield createResponse("SUCCESS")
    return 

class MovieGuideServicer(movie_pb2_grpc.MovieGuideServicer):
    def __init__(self):
	print "Server started.\nListening to commands....."

    def UserAction(self,request,context):
	if request.header == movie_pb2.ADD :
	    responses = addMovieService(request.argument)
	elif request.header == movie_pb2.SEARCH :
	    responses = searchMovieService(request.argument)    
	elif request.header == movie_pb2.UPDATE :
	    responses = updateMovieService(request.argument)    
	elif request.header == movie_pb2.DELETE:
	    responses = deleteMovieService(request.argument)    
	elif request.header == movie_pb2.SHOWALL:
	    responses = showMovieService(request.argument)
	else:
	    responses = createResponse("INVALID") 
	return responses	

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
    movie_pb2_grpc.add_MovieGuideServicer_to_server(MovieGuideServicer(),server) 
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
    	while True:
            time.sleep( 24*60*60 )
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__' :
    serve()
