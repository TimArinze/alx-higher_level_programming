$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
	var movies = data.results;
	var list = $("<ul>").attr("id", "list_movies");
	for (var i = 0; i < movies.length; i++) {
		var li = $("<li>").text(movies[i].title);
		list.append(li);
	}
	$("body").append(list);
});
