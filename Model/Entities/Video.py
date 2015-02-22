class VideoClass():
    """Class represents information about a media type - video"""
    def __init__(self, record_id, title, poster_image_url, trailer_youtube_url, imdb_url, wiki_url, years, duration):
        self.record_id = record_id
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url
        self.wiki_url = wiki_url
        self.years = years
        self.duration = duration
        self.typeName = self.__class__.__name__