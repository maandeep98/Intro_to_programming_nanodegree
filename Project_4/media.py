class Movie:
    """ Class to store movies """

    def __init__(self, movie_title, movie_rating, movie_release_date,
                 poster_image, trailer_youtube):
        """ Constructor method to store data in the objects
            created in entertainment_center.py """
        self.title = movie_title
        # The movie title is stored in 'self.title' for the object being given
        # values
        self.rating = movie_rating
        # The 'self.storyline' stores some information about story of the movie
        self.date = movie_release_date
        # 'self.date' represents the release date of the movie
        self.poster_image_url = poster_image
        # The URL for movie poster image is stored in 'self.poster_image_url'
        # for the object being given values
        self.trailer_youtube_url = trailer_youtube
        # The URL for movie youtube trailer is stored in
        # 'self.trailer_youtube_url' for the object being given values
