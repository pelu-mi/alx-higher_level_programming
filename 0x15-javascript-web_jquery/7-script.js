$(document).ready(function () {
	$(function () {
		$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
		function (data, textStatus) {
			$('div#character').text(data.name);
		});
	});
});