var http = require("http");
var url = require("url");

http.createServer(function (request, response) {

	console.log("--------------------------------------")
	console.log("The relative URL of the current request: " + request.url + "\n")
	var url_parts = url.parse(request.url, true);



	if (url_parts.pathname == '/submit') {

		////////////////////To jest nasz kod //////////////////////////

		var filePath = url_parts.query['name'];  // Pobranie ścieżki 

		response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" }); // ?

		const fs = require('fs');		// Importowanie modułu 


		fs.exists(filePath, (exists) => {  // Jeśli ścieżka istnieje 
			if (exists) {
			
				fs.readFile(filePath, 'utf8', function (err, contents) { // asynchroniczne czytanie pliku 
					if (!err) {
						response.write("PLIK\n" + contents);
						response.end();
					}
					else {
						return;
					}

				});
		
				fs.readdir(filePath, (err, entries) => {
					if (!err) {
						response.write("KATALOG	" + entries);
						response.end();
					}
					else {
						return;
					}
				});

			}
			else {
				response.write("Nie ma takiego pliku");
				response.end();
				return;
			}
		});

		////////////////////////////////////////////////////////////		

	}
	else {
		console.log("Creating a response header")
		response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });

		console.log("Creating a response body")
		response.write('<form method="GET" action="/submit">');
		response.write('<label for="name">Give your name</label>');
		response.write('<input name="name">');
		response.write('<br>');
		response.write('<input type="submit">');
		response.write('<input type="reset">');
		response.write('</form>');
		response.end();
		console.log("Sending a response")
	}
}).listen(8080);
console.log("The server was started on port 8080");
console.log("To end the server, press 'CTRL + C'");