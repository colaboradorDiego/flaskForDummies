# README #

# How to build a Real-Time streaming Quote Widget
	Bueno
	Real-Time data esto lo tengo que ver
	https://developers.refinitiv.com/en/article-catalog/article/how-to-build-a-real-time-streaming-quote-widget
	

# google API examples

	start server
		este es el servidor que publica las paginas que detallamos a continuacion
		python simpleServer.py
		
	paginas:
		http://127.0.0.1:5000/statictable
			el frontend utiliza el javascript google.visualization.DataTable para mostrar datos
			mediante un grafico de tabla google.visualization.Table. No hay interaccion con el servidor.
			Todos los datos estan en el mismo fronend.
	
	
		http://127.0.0.1:5000/pie
			El frontend utiliza el javascript google.visualization.arrayToDataTable 
			para mostrar los datos del servidor en un grafico de torta google.visualization.PieChart
			
			
		http://127.0.0.1:5000/dinamictable
			El frontend utiliza javascript puro para mostrar los datos del servidor en una tabla
			
		http://127.0.0.1:5000/semistatictable
			El frontend utiliza el javascript de google.visualization.DataTable para mostrar
			los datos del servisor en un grafico de table google.visualization.Table


# geekLogin example
	https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
	
	Flask mysql client
		pip install flask-mysqldb
	
	MySql Server
		mysql -> VirtualBox en mi pc -> linux Debian (192.168.0.101)
		root:usuario
	
	run:
		python simpleLogin.py
		now browse http://127.0.0.1:5000 to open login page
		
	


# Flask
	https://flask.palletsprojects.com/en/1.1.x/
	Quickstart
		https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
	
	We use decorator to tell Flask what URL should trigger our function.
	En este ej tenemos asociada la ruta 'miruta' con la funcion miruta()
		@app.route('miruta')
		def miruta() {
			bla bla bla
	
	To build a URL to a specific function, use the url_for() function
	En este ej url_for ejecuta la ruta o funcion 'miruta'
		return url_for('miruta')
		
	Formularios
		https://www.youtube.com/watch?v=g7Usra5trqk&list=PLBO4apWPK7b7K6c-jpEI0zflZYDjVp7cd&index=11
		
	
	Ademas estoy aprendiendo CSS, esta plantilla es puro hobby
		google/static/css/gridCss.css
		mas detalle en: https://developer.mozilla.org/es/docs/Web/CSS/CSS_Grid_Layout
	
	
# Flask & JavaScript
	Passing variables from Flask to JavaScript
		la magia de como enviar datos desde python a javascript pasa por el render_template
		https://stackoverflow.com/questions/37259740/passing-variables-from-flask-to-javascript/37260465

# Flask & JSON
	As of Flask 1.1.0, you can now directly return a python dict, and it will be automatically jsonify'd by Flask.
	If you want to return a different json-serializable object, you can import and use jsonify
	

### Google Developer: Display live data on your site
	https://developers.google.com/chart
	https://roytuts.com/google-pie-chart-using-python-flask/
	
	Visualization: Table
		https://developers.google.com/chart/interactive/docs/gallery/table
		
	DataTables and DataViews
		https://developers.google.com/chart/interactive/docs/datatables_dataviews#datatablesdataviews
		

