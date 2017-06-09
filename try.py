import movie_pb2
import sys

cinema = movie_pb2.Movie()
cinema.name = "baby"
cinema.genres.extend([movie_pb2.ADVENTURE,movie_pb2.DRAMA])
cinema.actors.extend(["bekkam" , "venkata" ,"aditya"])
cinema.runTime = 128

date = cinema.releaseDate
date.day = 26
date.month = movie_pb2.MAY
date.year = 1996


review = cinema.reviews.add()
review.userName = "raghu"
review.rating = 9
reviewDate = review.date
reviewDate.day = 20
reviewDate.month = movie_pb2.MAY
reviewDate.year = 2004


review = cinema.reviews.add()
review.userName = "dhoni"
review.rating = 7
reviewDate = review.date
reviewDate.day = 7
reviewDate.month = movie_pb2.JULY
reviewDate.year = 2007

print cinema
