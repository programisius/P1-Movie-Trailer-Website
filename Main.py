from Model.Managers.MovieManager import MovieManagerClass as MovieManager
from Model.Managers.TvShowManager import TvShowManagerClass as TvShowManager
import custom_fresh_tomatoes

# Get objects inherited from Video type lists
movies = MovieManager().ListMovies();
tvShows = TvShowManager().ListTvShows();
# Build website HTML file and show with default OS browser
custom_fresh_tomatoes.open_videos_page({ 'movies' : movies, 'tvShows' : tvShows})