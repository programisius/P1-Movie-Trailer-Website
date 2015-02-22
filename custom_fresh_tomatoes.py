import webbrowser
import os
import re
import json

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
    <link rel="stylesheet" type="text/css" media="screen" href="public/css/style.css">
    <script>
        var movieData = JSON.parse('{video_data}');
    </script>
    <script type="text/javascript" charset="utf-8" src="public/js/common.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
    <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">    
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
                    <div class="scale-media" id="trailer-video-container"></div>
                    <div class="modal-footer">
                        <table id="modal-footer-movie-tbl" style="display:none">
                            <tr>
                                <td>
                                    <h3 id="modal-footer-movie-title-lbl"></h3>
                                </td>
                                <td rowspan="4">
                                    <a id="modal-footer-movie-imdb-link" href="#" target="_blank" class="external-info"><img src="public/images/imdb-icon.png" width="50px" height="50px"/></a>
                                    <a id="modal-footer-movie-wiki-link" href="#" target="_blank" class="external-info"><img src="public/images/wiki-icon.png" width="45px" height="50px" /></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Years: </strong> <span id="modal-footer-movie-years-lbl"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Duration: </strong> <span id="modal-footer-movie-duration-lbl"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Directed by: </strong> <span id="modal-footer-movie-director-lbl"></span>
                                </td>
                            </tr>
                        </table>
                        <table id="modal-footer-tvshow-tbl" style="display:none">
                            <tr>
                                <td>
                                    <h3 id="modal-footer-tvshow-title-lbl"></h3>
                                </td>
                                <td rowspan="5">
                                    <a id="modal-footer-tvshow-imdb-link" href="#" target="_blank" class="external-info"><img src="public/images/imdb-icon.png" width="50px" height="50px"/></a>
                                    <a id="modal-footer-tvshow-wiki-link" href="#" target="_blank" class="external-info"><img src="public/images/wiki-icon.png" width="45px" height="50px" /></a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Years: </strong> <span id="modal-footer-tvshow-years-lbl"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Duration: </strong> <span id="modal-footer-tvshow-duration-lbl"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Seasons: </strong> <span id="modal-footer-tvshow-seasons-lbl"></span>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <strong>Original TV stations: </strong> <span id="modal-footer-tvshow-tv-station-lbl"></span>
                                </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Main Page Content -->
        <div class="container">
            <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="container">
                    <div class="navbar-header">
                        <a class="navbar-brand" href="#"><img class="logo-img" width="23px" height="23px" src="public/images/tomato-icon.png" alt="Brand" />Fresh Tomatoes Movie Trailers</a>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="content">
            <div class="container">
                <div class="page-nav">
                    <a id="movie-btn" href="#" class="btn-nav selected-btn">Movies</a>
                    <a id="tvShow-btn" href="#" class="btn-nav">TV Shows</a>
                </div>
            </div>
        
            <div class="container">
                <div id="movie-pnl">
                        {movie_tiles}
                </div>
                <div id="tvShow-pnl" style="display:none">
                    {tvShow_tiles}
                </div>
            </div>
        </div>
    </body>
</html>
'''

# A single video entry html template
video_tile_content = '''
<div id="{tile_id}" class="col-md-6 col-lg-4 {tile_class}-tile video-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="{img_height}">
    <h2>{video_title}</h2>
</div>
'''

def create_video_tiles_content(videos, tile_class):
    # The HTML content for this section of the page
    content = ''
    
    img_height = 342
    if tile_class == 'tvShow':
        img_height = 200
    
    index = 1
    for video in videos:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', video.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', video.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the video with its content filled in
        content += video_tile_content.format(
            tile_id = video.record_id,
            img_height = img_height,
            tile_class = tile_class,
            video_title=video.title,
            poster_image_url=video.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
        index += 1
    return content

def open_videos_page(videos):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    # Get items from videos dictionary if exist
    movies = videos['movies'] if 'movies' in videos else []    
    tvShows = videos['tvShows'] if 'tvShows' in videos else []
    # Merge list and convert result to JSON
    mergedList = movies + tvShows
    mergedListJson = json.dumps([v.__dict__ for v in mergedList])
    main_page_head_formated = main_page_head.format(video_data=mergedListJson)
    
    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_video_tiles_content(movies, 'movie'), tvShow_tiles=create_video_tiles_content(tvShows, 'tvShow'))

    # Output the file
    output_file.write(main_page_head_formated + rendered_content)
    output_file.close()

    # Open the output file in the browser
    url = os.path.abspath(output_file.name)
    # Open in a new tab, if possible
    webbrowser.open('file://' + url, new=2) 