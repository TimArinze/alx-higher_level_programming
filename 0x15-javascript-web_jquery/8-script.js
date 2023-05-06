const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(url, (data) => {
	const movies = data.results;
	movies.map((movie) => {
		$("UL#list_movies").append($("<li></li>").text(movie.title));
	});
});
