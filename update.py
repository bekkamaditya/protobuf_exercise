import sys
import movie_pb2
import pickle
import bsddb3

def updateMovie() :
    while True:
        name = raw_input("Movie name to be updated: ")
        flag = True
        index = -1 ;
	db = bsddb3.hashopen('movies.db','c')
        for key in db.keys() :
            index = index + 1
	    movie = pickle.loads( db[key] )
	    if movie.name == name:
		while True:
		    print "1.Name\n2.Directors\n3.Actors\n4.Genres\n5.Run time\n6.Production House\n7.Country\n8.Release Date:\n9.Languages:\n"
                    field = int( raw_input("Enter field to be updated(enter choice no. ): " ))
		    if field == 1:
			movie.name = raw_input("Enter updated movie name: ")
		    elif field == 5:
			movie.runTime = int( raw_input("Enter updated run time: ") )
		    elif field == 6:
			movie.productionHouse = raw_input("Enter updated productionHouse: ")
		    elif field == 7:
			movie.country = raw_input("Enter updated country: ")
		    elif field == 3:
			del movie.actors[:]
			act_list = raw_input("Enter updated actors list(comma separated list): ")
			while act_list == ""  :
			    act_list = raw_input("List cannot be empty.Please enter: ")
			for actor in act_list.split(','):
			    movie.actors.append(actor)
		    elif field == 2:
			del movie.directors[:] 
			dir_list = raw_input("Enter updated directors list(comma separated list): ")
			while dir_list == ""  :
			    dir_list = raw_input("List cannot be empty.Please enter: ")
			for director in dir_list.split(','):
			    movie.directors.append(director)
		    elif field == 9:
			del movie.languages[:]
			lan_list = raw_input("Enter updated languages list(comma separated list): ")
			while lan_list == ""  :
			    lan_list = raw_input("List cannot be empty.Please enter: ")
			for language in lan_list.split(','):
			    movie.languages.append(language)
		    elif field == 4:    
			genres = raw_input("Select genre(comma separated list): adventure/drama/sci_fi ")
			while genres == "" :
        		    genres = raw_input("List cannot be empty.Plese enter. ")
			del movie.genres[:]
    			for genre in genres.split(','):
        		    if genre.upper() == "ADVENTURE" :
            		 	movie.genres.append(movie_pb2.ADVENTURE)
        		    elif genre.upper() == "SCI_FI" :
            		    	movie.genres.append(movie_pb2.SCI_FI)
        		    elif genre.upper() == "DRAMA" :
           		    	movie.genres.append(movie_pb2.DRAMA)
		    elif field == 8:
			date = raw_input("Release date(DD/MM/YYYY): ")
    			list_temp = date.split("/");
    			movie.releaseDate.day = int( list_temp[0] )
    			mon = int(list_temp[1]) ;
    			if mon == 1:
        		    movie.releaseDate.month = movie_pb2.JANUARY
    			elif mon == 2:
        		    movie.releaseDate.month = movie_pb2.FEBRUARY
    			elif mon == 3:
        		    movie.releaseDate.month = movie_pb2.MARCH
    			elif mon == 4:
        		    movie.releaseDate.month = movie_pb2.APRIL
    			elif mon == 5:
        		    movie.releaseDate.month = movie_pb2.MAY
    			elif mon == 6:
        		    movie.releaseDate.month = movie_pb2.JUNE
    			elif mon == 7:
        		    movie.releaseDate.month = movie_pb2.JULY
    			elif mon == 8:
        		    movie.releaseDate.month = movie_pb2.AUGUST
    			elif mon == 9:
        		    movie.releaseDate.month = movie_pb2.SEPTEMBER
    			elif mon == 10:
        		    movie.releaseDate.month = movie_pb2.OCTOBER
    			elif mon == 11:
        		    movie.releaseDate.month = movie_pb2.NOVEMBER
    			elif mon == 12:
        	 	    movie.releaseDate.month = movie_pb2.DECEMBER
    			movie.releaseDate.year = int( list_temp[2] )
		    db[key] = pickle.dumps(movie) 
		    flag = False
		    if raw_input("Do you want to update any other fields(or leave blank to finish): ") == "" :
			break 
                break
	if index==-1 :
	    print "No movies to show" 
	    break 
        if flag:
            print "Movie not found.Continuing...."
	if raw_input("Do you want to update another movie(or leave blank to finish): ") == "" :
	    break 
