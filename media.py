class Movie:
    """Represents a movie.

    Attributes:
        title: String representing movie title.
        storyline: Short description of movie's plot as string.
        poster_image_url: Url pointing to a movie image poster.
        trailer_youtube_url: Url linking to movie's trailer on youtube.com.
        release_date: Official premiere date of the movie.
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, release_date):
        """Returns a new Movie object"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
