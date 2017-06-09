import pickle
import bsddb3
import movie_pb2
import sys

def PromptForMovieDetails():
    movie = movie_pb2.Movie()
    # File to database storage
    key = raw_input("Movie name: ")
    movie.name = key

    dir_list = raw_input("Directors(comma separated list): ")
    while dir_list == "" :
        dir_list = raw_input("List cannot be empty.Plese enter. ")
    for director in dir_list.split(','):
        movie.directors.append(director) ;

    act_list = raw_input("Actors(comma separated list): ")
    while act_list == "" :
        act_list = raw_input("List cannot be empty.Plese enter. ")
    for actor in act_list.split(','):
        movie.actors.append(actor) ;

    genres = raw_input("Select genre(comma separated list): adventure/drama/sci_fi ")
    while genres == "" :
        genres = raw_input("List cannot be empty.Plese enter. ")
    for genre in genres.split(','):
        if genre.upper() == "ADVENTURE" :
            movie.genres.append(movie_pb2.ADVENTURE)
        elif genre.upper() == "SCI_FI" :
            movie.genres.append(movie_pb2.SCI_FI)
        elif genre.upper() == "DRAMA" :
            movie.genres.append(movie_pb2.DRAMA)

    languages = raw_input("languages released(Comma separated list): ")
    while languages == "" :
        languages = raw_input("List cannot be empty.Plese enter. ")
    for language in languages.split(','):
        movie.languages.append(language)

    movie.runTime = int( raw_input("Run time of movie(in minutes): "))

    producer = raw_input("Production company(optional): ")
    if producer != "" :
        movie.productionHouse = producer ;

    country = raw_input("Country(optional): ")
    if country != "" :
        movie.country = country ;

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

    while True :
        response = raw_input("Do you want to add a review(leave blank otherwise)?: ")
        if response == ""  :
            break ;
        review = movie.reviews.add() ;
        review.userName = raw_input("User name: ")
        review.rating = int(raw_input("Rating: "))
        review.comment = raw_input("Comment: ")
        date = raw_input("Date(DD/MM/YYYY): ")
        list_temp = date.split("/");
        review.date.day = int( list_temp[0] )
        mon = int(list_temp[1]) ;
        if mon == 1:
            review.date.month = movie_pb2.JANUARY
        elif mon == 2:
            review.date.month = movie_pb2.FEBRUARY
        elif mon == 3:
            review.date.month = movie_pb2.MARCH
        elif mon == 4:
            review.date.month = movie_pb2.APRIL
        elif mon == 5:
            review.date.month = movie_pb2.MAY
        elif mon == 6:
            review.date.month = movie_pb2.JUNE
        elif mon == 7:
            review.date.month = movie_pb2.JULY
        elif mon == 8:
            review.date.month = movie_pb2.AUGUST
        elif mon == 9:
            review.date.month = movie_pb2.SEPTEMBER
        elif mon == 10:
            review.date.month = movie_pb2.OCTOBER
        elif mon == 11:
            review.date.month = movie_pb2.NOVEMBER
        elif mon == 12:
            review.date.month = movie_pb2.DECEMBER
        review.date.year = int( list_temp[2] )
    print movie
    # File to database storage
    db = bsddb3.hashopen('movies.db','c')
    db[key] = pickle.dumps(movie)

def addMovie():
    # File to database storage
    PromptForMovieDetails()
