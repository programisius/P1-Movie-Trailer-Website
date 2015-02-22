// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, #trailer', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
$(document).on('click', '#trailer .modal-content', function (event) {
    event.stopPropagation();
});

$(document).on('click', '.video-tile', function (event) {
    // Take Video type information from JSON object and load it in modal window footer
    var tileId = $(this).attr('id');
    var result = $.grep(movieData, function(e){ return e.record_id == tileId; });
    if (result.length > 0) {
        var typeName = result[0].typeName.replace("Class", "").toLowerCase();
        switch(typeName)
        {
            case 'movie':
            {
                $('#modal-footer-movie-director-lbl').text(result[0].director);
                break;
            }
            case 'tvshow':
            {
                $('#modal-footer-tvshow-seasons-lbl').text(result[0].seasons);
                $('#modal-footer-tvshow-tv-station-lbl').text(result[0].tv_station);
                break;
            }
        }
        $('.modal-footer table').hide();
        $('#modal-footer-'+ typeName +'-tbl').show();
        $('#modal-footer-'+ typeName +'-title-lbl').text(result[0].title);
        $('#modal-footer-'+ typeName +'-years-lbl').text(result[0].years);
        $('#modal-footer-'+ typeName +'-duration-lbl').text(result[0].duration + " minutes");
        $('#modal-footer-'+ typeName +'-imdb-link').attr('href', result[0].imdb_url);
        $('#modal-footer-'+ typeName +'-wiki-link').attr('href', result[0].wiki_url);
    }
    // Start playing the video whenever the trailer modal is opened
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});
// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});
$(document).on('click', '.external-info', function (event) {
    $('.hanging-close').click();
});
// Show "Movies" list and hide "TV shows" list
$(document).on('click', '#movie-btn', function (event) {
    event.preventDefault();
    
    $('#movie-pnl').show();
    $('#tvShow-pnl').hide();
    
    $('#movie-btn').addClass('selected-btn');
    $('#tvShow-btn').removeClass('selected-btn');
    
    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
});
// Show "TV shows" list and hide "Movies" list
$(document).on('click', '#tvShow-btn', function (event) {
    event.preventDefault();
    
    $('#tvShow-pnl').show();
    $('#movie-pnl').hide();
    
    $('#tvShow-btn').addClass('selected-btn');
    $('#movie-btn').removeClass('selected-btn');
    
    $('.tvShow-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
});