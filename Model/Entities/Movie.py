from Video import VideoClass as Video

class MovieClass(Video):
    """Class represents information about a movie"""
    def __init__(self, record_id, title, poster_image_url, trailer_youtube_url, imdb_url, wiki_url, years, duration, director):
        Video.__init__(self, record_id, title, poster_image_url, trailer_youtube_url, imdb_url, wiki_url, years, duration)
        self.director = director