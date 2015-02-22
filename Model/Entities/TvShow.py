from Video import VideoClass as Video

class TvShowClass(Video):
    """Class represents information about a TV show"""
    def __init__(self, record_id, title, poster_image_url, trailer_youtube_url, imdb_url, wiki_url, years, duration, seasons, tv_station):
        Video.__init__(self, record_id, title, poster_image_url, trailer_youtube_url, imdb_url, wiki_url, years, duration)
        self.seasons = seasons
        self.tv_station = tv_station