$(document).ready(function() {
    let endpoint = 'https://api.themoviedb.org/3/movie/now_playing'
    let apiKey = '3e4d90cc981994d2cf858de33c365791'
    let poster_path = 'https://image.tmdb.org/t/p/w500' // + poster_path
    let background_path = 'https://image.tmdb.org/t/p/w500' // + backdrop_path

    $.ajax({
        url: endpoint + "?api_key=" + apiKey + '&language=es-ES',
        contentType: "application/json",
        dataType: 'json',
        success: function(result){

            console.log(result);

        }
    })

});