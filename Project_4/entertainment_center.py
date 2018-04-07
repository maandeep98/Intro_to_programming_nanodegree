import media
import fresh_tomatoes

# importing python modules to organise code logically

# This is where new objects of the class Movie are created and are given
# respective values.

# fast_and_furious: movie title, movie storyline, Poster Image path,
# Youtube Trailer URL
fast_and_furious = media.Movie("Fast and Furious",
                               "6.6/10 IMDb rating",
                               " 3 April 2009",
                               r"img\ff.jpg",
                               "https://www.youtube.com/watch?v=N0ITWaDAcME")

# harry_potter: movie title, movie storyline, Poster Image path, Youtube
# Trailer URL
harry_potter = media.Movie("Harry Potter",
                           "7.6/10 IMDb rating",
                           "12 April 2002 (India)",
                           r"img\hp.jpg",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")

# lakshya: movie title, movie storyline, Poster Image path, Youtube Trailer URL
lakshya = media.Movie("Lakshya",
                      "7.9 IMDb rating",
                      "18 June 2004 (India)",
                      r"img\l.jpg",
                      "https://www.youtube.com/watch?v=YoKGmYyljmc")

# border: movie title, movie storyline, Poster Image path, Youtube Trailer URL
border = media.Movie("Border",
                     "7.9/10 IMDb rating",
                     "13 June 1997 (India)",
                     r"img\b.jpg",
                     "https://www.youtube.com/watch?v=aJ-sxaxkoD4")

# sarkar_3: movie title, movie storyline, Poster Image path, Youtube
# Trailer URL
sarkar_3 = media.Movie("Sarkar 3",
                       "4.8/10 IMDb rating",
                       " 12 May 2017 (India)",
                       r"img\s.jpg",
                       "https://www.youtube.com/watch?v=B27zvZRfeSo")

# iron_man: movie title, movie storyline, Poster Image path, Youtube
# Trailer URL
iron_man = media.Movie("Iron Man",
                       "7.9/10 IMDb rating",
                       "1 May 2008 (India)",
                       r"img\im.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

# creating an array of movies
movies = [fast_and_furious, harry_potter, lakshya, border, sarkar_3, iron_man]
fresh_tomatoes.open_movies_page(movies)
