$(document).ready(function () {
	$(function () {
		$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
		function (data, textStatus) {
			for (let movie of data.results) {
				let item = $('<li></li>').text(movie.title);
				$('ul#list_movies').append(item);
			}
		});
	});
});
