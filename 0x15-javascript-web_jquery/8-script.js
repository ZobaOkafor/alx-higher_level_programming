$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;
    movies.forEach(function(movie) {
      $('<li>').text(movie.title).appendTo('UL#list_movies');
    });
  });
});
